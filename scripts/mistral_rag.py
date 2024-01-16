# Import Modules
from llama_index.llms import Ollama
import qdrant_client
from pathlib import Path
from llama_index import download_loader
from llama_index import VectorStoreIndex, ServiceContext, SimpleDirectoryReader
from llama_index.storage.storage_context import StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStore
from datetime import datetime


def index_data(file_path):
    UnstructuredReader = download_loader("UnstructuredReader")
    loader = UnstructuredReader()
    docs = loader.load_data(file=file_path)
    
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y_%m_%d_%H-%M-%S")
    data_path = f"/home/ubuntu/Mistral-7B-RAG/data/uploaded_files/file_{formatted_time}/"
    client = qdrant_client.QdrantClient(path=data_path)

    vector_store = QdrantVectorStore(client=client, collection_name="mistral_data")

    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    
    llm = Ollama(model="mistral")
    service_context = ServiceContext.from_defaults(llm=llm, embed_model="local")
    
    index = VectorStoreIndex.from_documents(docs, service_context=service_context, storage_context=storage_context)
    
    return index


def query_data(query: str, index):
    chat_engine = index.as_chat_engine(chat_mode="condense_question", streaming=True)
    response = chat_engine.chat(query)
    return response.response