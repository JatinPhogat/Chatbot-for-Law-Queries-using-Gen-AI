import os
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

def embed_and_save_documents():
    print("Loading local embedding model for legal documents...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    print("✓ Embedding model loaded")
    
    loader = PyPDFDirectoryLoader("./data")
    print("Initialized PDF loader for legal documents")

    docs = loader.load()
    print(f"Loaded {len(docs)} legal documents")

    unique_files = set()
    for doc in docs:
        file_name = os.path.basename(doc.metadata.get('source', 'Unknown'))
        if file_name not in unique_files:
            print(f"    File loaded: {file_name}")
            unique_files.add(file_name)

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    final_documents = text_splitter.split_documents(docs)
    print(f"Split into {len(final_documents)} chunks")

    for doc in final_documents:
        if 'source' in doc.metadata:
            source_file = doc.metadata['source']
            doc.metadata['source'] = os.path.basename(source_file)
        else:
            doc.metadata['source'] = os.path.basename(loader.directory)

    print("Creating embeddings and saving to Chroma (legal knowledge base)...")
    vectorstore = Chroma.from_documents(final_documents, embeddings, persist_directory="legal_vector_store")
    print(f"\n✓ Legal knowledge base saved at 'legal_vector_store' with {len(final_documents)} chunks")

embed_and_save_documents()
