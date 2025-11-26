"""
NyaySetu - Core Logic Module
Legal AI Assistant Backend
"""

import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains import ConversationalRetrievalChain

# Load environment variables
load_dotenv()

class NyaySetu:
    """NyaySetu Legal AI Assistant"""
    
    def __init__(self):
        """Initialize the legal assistant"""
        self.groq_api_key = os.getenv("GROQ_API_KEY")
        self.embeddings = None
        self.db = None
        self.qa_chain = None
        self._initialize_components()
    
    def _initialize_components(self):
        """Initialize embeddings, database, and QA chain"""
        # Load embeddings
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        
        # Load vector database
        self.db = Chroma(
            persist_directory="legal_vector_store",
            embedding_function=self.embeddings
        )
        self.db_retriever = self.db.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 4}
        )
        
        # Define prompt template for legal domain
        prompt_template = """
<s>[INST]
You are NyaySetu, a helpful AI legal assistant. Provide clear answers about Indian law, legal procedures, and rights.

Instructions:
- Answer based on the CONTEXT provided and legal knowledge
- Keep responses concise (2-3 sentences max) and easy to understand for common people
- Use simple language, avoid complex legal jargon unless necessary
- If asked about non-legal topics, politely redirect: "I'm specialized in Indian law and legal matters. For that topic, I'd recommend consulting a relevant expert. Is there anything about law or legal procedures I can help you with?"
- If the CONTEXT doesn't have the information, say: "I don't have specific information about that in my knowledge base. For accurate legal advice, please consult a qualified lawyer."
- Always add: "Note: This is general information, not legal advice. Consult a lawyer for your specific case."

CONTEXT: {context}

CHAT HISTORY: {chat_history}

USER QUESTION: {question}

YOUR ANSWER:
</s>[INST]
"""
        
        prompt = PromptTemplate(
            template=prompt_template,
            input_variables=['context', 'question', 'chat_history']
        )
        
        # Initialize LLM
        llm = ChatGroq(
            groq_api_key=self.groq_api_key,
            model_name="llama-3.3-70b-versatile"
        )
        
        # Create QA chain
        self.qa_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=self.db_retriever,
            combine_docs_chain_kwargs={'prompt': prompt}
        )
    
    def ask(self, question: str, chat_history: list = None) -> str:
        """
        Ask a question to NyaySetu
        
        Args:
            question: User's question
            chat_history: List of (role, message) tuples
            
        Returns:
            Answer from the legal assistant
        """
        if chat_history is None:
            chat_history = []
        
        result = self.qa_chain.invoke({
            "question": question,
            "chat_history": chat_history
        })
        
        return result["answer"]

# Singleton instance
_nyaysetu_instance = None

def get_nyaysetu():
    """Get or create NyaySetu instance"""
    global _nyaysetu_instance
    if _nyaysetu_instance is None:
        _nyaysetu_instance = NyaySetu()
    return _nyaysetu_instance
