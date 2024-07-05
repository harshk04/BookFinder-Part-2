from langchain_qdrant import Qdrant
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from qdrant_client import QdrantClient

# Initialize the embeddings model
model_name = "BAAI/bge-large-en"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}
embeddings = HuggingFaceBgeEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

# Initialize the Qdrant client
url = "http://localhost:6333"
client = QdrantClient(
    url=url, prefer_grpc=False
)

# Initialize the Qdrant database
db = Qdrant(client=client, embeddings=embeddings, collection_name="task2")

# Perform a semantic search in all collections
query = "Find top 100 books in fiction genre."

docs = db.similarity_search_with_score(query=query, k=5)
context = "\n".join([doc.page_content for doc, score in docs])

print(context)