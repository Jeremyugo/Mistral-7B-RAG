import streamlit as st
from pathlib import Path
import tempfile
from llama_index import download_loader
import sys
from llama_index.llms import Ollama
import qdrant_client
from pathlib import Path
from llama_index import download_loader
from llama_index import VectorStoreIndex, ServiceContext, SimpleDirectoryReader
from llama_index.storage.storage_context import StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStore


sys.path.append("/home/ubuntu/Mistral-7B-RAG/")
from scripts.mistral_rag import index_data, query_data

@st.cache_data
def create_temp_file_path(file):
    file_content = file.read()
    file_extension = ".txt" if file.type == "text/plain" else ".json"
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as temp_file:
        temp_file.write(file_content)
        tempfile_path = temp_file.name
        return tempfile_path    


@st.cache_resource
def get_index(file_path):
    return index_data(file_path)


#@st.cache_resource
def stream_respose(query, index):
    response = query_data(query, index)
    return response



st.title(f'Mistral-7B RAG App ⚙️🗃️')
st.write("This is a Retrieval Augmented Generation streamlit app powered by the open-source Mistral 7B LLM and llama-index.")


file = st.file_uploader('Upload your document', type=['txt', 'json'])


if file is not None:
    button = st.button("clear chat history")
    if button and "message" in st.session_state:
        del st.session_state["message"]

        
    file_path = create_temp_file_path(file)
    indices = get_index(file_path)
    query = st.chat_input('Query your data')
    
    if "message" not in st.session_state: # Initialize the chat message history
        st.session_state["message"] = [
            {"role": "assistant", "content": "Ask me a question about your document!"}
        ]
        
    if query:
        st.session_state["message"].append({"role": "user", "content": query})
        
    for message in st.session_state["message"]:
        with st.chat_message(message["role"]):
            st.write(message["content"])
                
    if st.session_state["message"][-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = stream_respose(query=query, index=indices)
                st.write(response)
                message = {"role": "assistant", "content": response}
                st.session_state["message"].append(message)