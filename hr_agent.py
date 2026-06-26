from langchain_ollama import ChatOllama,OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain.tools import tool
from datetime import datetime
from langchain_community.vectorstores import FAISS
from langchain_classic.agents import AgentExecutor,create_tool_calling_agent
from typing import List
from pydantic import BaseModel

#Model
llm=ChatOllama(model="qwen3:4b")

chat_history=InMemoryChatMessageHistory()


embeddings=OllamaEmbeddings(model="nomic-embed-text")

vectordb=FAISS.load_local(
    "hr_vector_db",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever=vectordb.as_retriever(
    search_kwargs={"k":3}
)

@tool
def experiencecalculator(start_year:int)->str:
    """Calculate the candidate experience"""
    return str(
        datetime.now().year - start_year
    )

@tool
def eligibility_checker(skills:str)->str:
    """Calculate candidate eligibility"""
    required={
        "python",
        "sql",
        "git"
    }

    candidate ={
        skills.strip().lower()
        for skill in skills.split(",")
    }

    missing=required-candidate

    if len(missing)==0:
        return "Eligible"
    return "Not Eligible.Missing "+",".join(missing)

@tool
def generate_questions(skills:str)->str:
    """Generate interview questions"""

    prompt=f"""Generate 5 interview questions 
                for {skills}"""
    
    return llm.invoke(prompt).content


@tool
def company_policy_search(question:str)->str:
    """Search company document"""

    docs=retriever.invoke(question)

    context="\n".join(
        doc.page_content
        for doc in docs
    )

    prompt=f"""Answer only from the provided context.
    Context:{context}
    Question:{question}"""

    result=llm.invoke(prompt)
    return result.content


tools=[generate_questions,eligibility_checker,company_policy_search,experiencecalculator]

prompt=ChatPromptTemplate.from_messages(
    [
        (
            "system","""You are an HR recruiting assistant.
            
            use tools whenever required
            
            if the user asks:
                leave policy
                notice period
                working hours
                job description
                company policy
            always use company_policy_search
            """
        ),
        ("human","{input}"),
        ("placeholder","{agent_scratchpad}")
    ]
)

agent=create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

agent_executor=AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

class Candidate(BaseModel):
    name:str
    experience:int
    skills:List[str]

structured_llm=llm.with_structured_output(Candidate)

while True:

    user_input = input("\nYou : ")

    if user_input.lower() == "exit":
        break

    if user_input.startswith("resume:"):

        resume = user_input.replace(
            "resume:",
            ""
        )

        candidate = structured_llm.invoke(
            f"""
            Extract:

            Name
            Experience
            Skills

            Resume:

            {resume}
            """
        )

        print("\nCandidate Details")
        print(candidate)

        continue

    response = agent_executor.invoke(
        {
            "input": user_input
        }
    )

    print(
        "\nAssistant:",response["output"]
    )