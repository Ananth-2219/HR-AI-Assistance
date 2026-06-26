import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

documents=[]

docs_dir = r"C:\Users\anant\vscode\AI\HR-AI-Assistance\documents"

for file in os.listdir(docs_dir):
    path=os.path.join(docs_dir,file)
    loader=TextLoader(path)
    docs=loader.load()
    documents.extend(docs)

print(f"loaded {len(documents)} Documents")

splitter=RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks=splitter.split_documents(documents)

print(f"created {len(chunks)} chunks")

embedding = OllamaEmbeddings(
    model="nomic-embed-text"
)

vectordb=FAISS.from_documents(chunks,embedding)

vectordb.save_local(
    "hr_vector_db"

)

print(" db created")