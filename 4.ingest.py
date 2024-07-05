from langchain_qdrant import Qdrant
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

file_paths = ["llm.txt", "scrap1.txt", "scrap2.txt"]

documents = []
for file_path in file_paths:
    loader = TextLoader(file_path)
    documents.extend(loader.load())

text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=50)
texts = text_splitter.split_documents(documents)

model_name = "BAAI/bge-large-en"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}
embeddings = HuggingFaceBgeEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

url = "http://localhost:6333"
qdrant = Qdrant.from_documents(
    texts,
    embeddings,
    url=url,
    prefer_grpc=False,
    collection_name="task2"
)

print("Successfully Created!")
