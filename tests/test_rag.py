import pytest
from langchain.embeddings import OpenAIEmbeddings
from chromadb import Client

def test_embedding_and_retrieval():
    embeddings = OpenAIEmbeddings()
    client = Client()
    collection = client.create_collection('energy_docs')
    doc = "Oil production is influenced by reservoir pressure."
    emb = embeddings.embed_query(doc)
    collection.add(documents=[doc], embeddings=[emb])
    results = collection.query(query_embeddings=[emb], n_results=1)
    assert results['documents'][0][0] == doc
