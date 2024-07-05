from langchain_qdrant import Qdrant
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from qdrant_client import QdrantClient, models
from gradio_client import Client
import hashlib
import uuid
import sys


def get_prompts(query, context):
    client = Client("harshk04/TextGeneration")
    result = client.predict(
        message=f"Give a correct output of the question '{query}' using the context: '{context}'",
        system_message="You are a friendly chatbot",
        max_tokens=800,
        temperature=0.7,
        top_p=0.95,
        api_name="/chat"
    )

    list_prompts = result.split("\n")
    list_prompts = [prompt[3:] for prompt in list_prompts if prompt and prompt[0].isdigit()]

    return list_prompts


model_name = "BAAI/bge-large-en"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}
embeddings = HuggingFaceBgeEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

url = "http://localhost:6333"
client = QdrantClient(
    url=url, prefer_grpc=False
)

db = Qdrant(client=client, embeddings=embeddings, collection_name="task2")

cache_collection_name = "cache"

collections = [col.name for col in client.get_collections().collections]
if cache_collection_name not in collections:
    vectors_config = models.VectorParams(size=1024, distance=models.Distance.COSINE)
    client.create_collection(collection_name=cache_collection_name, vectors_config=vectors_config)

cache_db = Qdrant(client=client, embeddings=embeddings, collection_name=cache_collection_name)

def hash_query(query):
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, query))

def semantic_search_with_cache(query, k=5):
    query_hash = hash_query(query)
    
    cache_results = cache_db.similarity_search_with_score(query=query_hash, k=1)
    
    if cache_results:
        cached_context = cache_results[0][0].page_content
        print("***CACHE HIT***")  
        print("\n")
        return cached_context
    
    docs = db.similarity_search_with_score(query=query, k=k)
    context = "\n".join([doc.page_content for doc, score in docs])
    
    from langchain_core.documents import Document 
    cache_db.add_documents([Document(page_content=context)], ids=[query_hash])
    print("***CACHE MISS, STORING RESULT***")  
    print("\n")
    return context

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python 5.main.py <query>")
        sys.exit(1)

    query = sys.argv[1]
    context = semantic_search_with_cache(query)

    books = get_prompts(query, context)

    print(f"\nHere is the result for '{query}':\n")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book}")
