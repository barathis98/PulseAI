import os
from openai import OpenAI
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_chroma import Chroma
from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA

load_dotenv()


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),  
)

def load_vector_store(persisit_directory: str):
    try:
        embedding = OpenAIEmbeddings()
        vector_store = Chroma(persist_directory= persisit_directory, embedding_function=embedding)
        return vector_store
    except Exception as e:
        print(f"Failed to load vector store: {e}")
        return None
    

def create_qa_chain(vector_store):
    retriever = vector_store.as_retriever(search_type = "similarity", search_kwargs = {"k": 3})

    prompt_template = PromptTemplate(
        input_variables = ["context", "question"],
        template = (
            "You are a highly knowledgeable assistant. You are helping a student with their examination preparation. Use the following context to answer the question. Dont hallucinate and answer from the context\n"
            "Context: {context}\n\n"
            "Question: {question}\n"
            "Answer:"
        )
    )

    model = ChatOpenAI(model = 'gpt-4o-mini', temperature = 0)
    qa_chain = RetrievalQA.from_chain_type(retriever = retriever, chain_type_kwargs = {"prompt":prompt_template}, llm = model, chain_type = "stuff")

    return qa_chain

def ask_question(question: str):
    vector_store = load_vector_store("chroma_db")

    qa_chain = create_qa_chain(vector_store)


    answer = qa_chain({"query": question})

    return answer['result']


