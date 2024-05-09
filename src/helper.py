from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
import time
import itertools
import openai
from  pinecone import Pinecone
limit = 3750
#Extract data from the PDF
def load_pdf(data):
    loader = DirectoryLoader(data,
                    glob="*.pdf",
                    loader_cls=PyPDFLoader)
    
    documents = loader.load()

    return documents



#Create text chunks
def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 20)
    text_chunks = text_splitter.split_documents(extracted_data)

    return text_chunks



#download embedding model
def download_hugging_face_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings


def chunks(iterable, batch_size=100):
    """A helper function to break an iterable into chunks of size batch_size."""
    it = iter(iterable)
    chunk = tuple(itertools.islice(it, batch_size))
    while chunk:
        yield chunk
        chunk = tuple(itertools.islice(it, batch_size))







    #  --------------------------------------------------------------------------   
    
PINECONE_API_KEY = "ee7860c7-aab7-4bec-bd66-0521c66fe048"
openai.api_key = 'sk-proj-UPUTw85MiYiBtYvOIXwUT3BlbkFJLrk4Y6aNyd39U6udFgMG'

embeddings = download_hugging_face_embeddings()

pc=Pinecone(PINECONE_API_KEY)
index = pc.Index("medic-bot")


def retrieve(query,conversation_history):
    vector=embeddings.embed_query(query)
    # get relevant contexts
    contexts = []
    for message in conversation_history:
        contexts.append(f"{message['role'].capitalize()}: {message['content']}\n")
    time_waited = 0
    while (len(contexts) < 3 and time_waited < 60 * 12):
        res=index.query(vector=vector,top_k=3,include_values=True,include_metadata=True)
        contexts = contexts + [
            x['metadata']['text'] for x in res['matches']
        ]
        print(f"Retrieved {len(contexts)} contexts, sleeping for 15 seconds...")
        time.sleep(15)
        time_waited += 15

    if time_waited >= 60 * 12:
        print("Timed out waiting for contexts to be retrieved.")
        contexts = ["No contexts retrieved. Try to answer the question yourself!"]


    # build our prompt with the retrieved contexts included
    prompt_start = (
        "Use the following pieces of information to answer the user's question.\
        If you don't know the answer, just say that you don't know, don't try to make up an answer.\n\n"+
        "Context:\n"
    )
    prompt_end = (
        f"\n\nQuestion: {query}\n Only return the helpful answer below and nothing else.\nAnswer:"
    )
    # append contexts until hitting limit
    for i in range(1, len(contexts)):
        if len("\n\n---\n\n".join(contexts[:i])) >= limit:
            prompt = (
                prompt_start +
                "\n\n---\n\n".join(contexts[:i-1]) +
                prompt_end
            )
            break
        elif i == len(contexts)-1:
            prompt = (
                prompt_start +
                "\n\n---\n\n".join(contexts) +
                prompt_end
            )
    return prompt




def complete(prompt):
    # instructions
    sys_prompt = "You are a helpful assistant that always answers questions."
    # query text-davinci-003
    res = openai.ChatCompletion.create(
        model='gpt-3.5-turbo-0613',
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )
    response=res['choices'][0]['message']['content'].strip()
    return response

def chatbot(query,conversation_history):
    query_with_contexts = retrieve(query,conversation_history)
    response=complete(query_with_contexts)
    conversation_history.append({"role": "user", "content":query})
    conversation_history.append({"role": "assistant", "content": response})
    return response,conversation_history