import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

DATA_FOLDER = "data"
VECTOR_STORE_FOLDER = "vector_store"

def load_text_files():
    documents = []
    for filename in os.listdir(DATA_FOLDER):
        if filename.endswith(".txt"):
            filepath = os.path.join(DATA_FOLDER, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
                documents.append(text)
    return documents


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    all_chunks = []
    for doc in documents:
        chunks = splitter.split_text(doc)
        all_chunks.extend(chunks)
    return all_chunks


def create_vector_store(chunks):
    # Embedding model — good & fast
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Creating embeddings... this may take 10–20 seconds...")
    vector_db = FAISS.from_texts(chunks, embedding_model)

    vector_db.save_local(VECTOR_STORE_FOLDER)
    print("Vector store saved successfully!")


if __name__ == "__main__":
    print("Loading text files...")
    docs = load_text_files()

    print("Splitting into chunks...")
    chunks = split_documents(docs)

    print(f"Total chunks created: {len(chunks)}")

    print("Storing in FAISS vector store...")
    create_vector_store(chunks)

    print("Ingestion Complete! BharatGPT is ready 🎉🇮🇳")
