from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from langchain.vectorstores import Pinecone
import itertools
from pinecone import Pinecone
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')



extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()

vector=[embeddings.embed_query(t.page_content) for t in text_chunks]
vectors=[]
for i,vec in enumerate(vector):
    vectors.append({'id':str(i),'values':vec,"metadata": {'text':text_chunks[i].page_content}})
#Initializing the Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY, pool_threads=30)
index_name="medic-bot"
index = pc.Index(index_name)

def chunks(iterable, batch_size=100):
    """A helper function to break an iterable into chunks of size batch_size."""
    it = iter(iterable)
    chunk = tuple(itertools.islice(it, batch_size))
    while chunk:
        yield chunk
        chunk = tuple(itertools.islice(it, batch_size))
with pc.Index('medic-bot', pool_threads=30) as index:

    async_results = [
        index.upsert(vectors=ids_vectors_chunk, async_req=True)
        for ids_vectors_chunk in chunks(vectors, batch_size=100)
    ]
    [async_result.get() for async_result in async_results]