import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter

VECTOR_STORE_FOLDER = "vector_store"

# Load FAISS DB
def load_vector_store():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.load_local(VECTOR_STORE_FOLDER, embeddings, allow_dangerous_deserialization=True)


# Streamlit UI
st.title("🇮🇳 BharatGPT – India's Knowledge Chatbot")

api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

if not api_key:
    st.warning("Please enter your API key to continue.")
    st.stop()

query = st.text_input("Ask anything about India… 🇮🇳")

if query:
    # Load FAISS DB
    db = load_vector_store()

    # Retrieve relevant chunks
    docs = db.similarity_search(query, k=4)

    # Convert retrieved docs into context
    context = "\n\n".join([d.page_content for d in docs])

    # LLM
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=api_key,
        temperature=0.2
    )

    # Prompt
    prompt = ChatPromptTemplate.from_template("""
    You are BharatGPT — an AI expert on India.
    Use ONLY the context below to answer.

    If the answer is not in the context, reply:
    "Sorry..I don't have idea about this.. I will study about this.."

    CONTEXT:
    {context}

    QUESTION:
    {question}
    """)

    final_prompt = prompt.format(context=context, question=query)

    # Generate answer
    response = llm.invoke(final_prompt)

    st.write("### Answer:")
    st.write(response.content)
