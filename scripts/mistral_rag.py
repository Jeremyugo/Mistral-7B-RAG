# Import Modules
from llama_index.llms import Ollama
import qdrant_client
from llama_index import VectorStoreIndex, ServiceContext, SimpleDirectoryReader
from llama_index.storage.storage_context import StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStore

def 