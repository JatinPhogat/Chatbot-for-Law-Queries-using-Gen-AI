"""
NyaySetu - Streamlit UI
Legal AI Assistant Interface
"""

import streamlit as st
from nyaysetu import get_nyaysetu

# Page config
st.set_page_config(
    page_title="NyaySetu - न्याय सेतु",
    page_icon="⚖️",
    layout="wide"
)

# Dark theme styling with law theme colors
st.markdown("""
    <style>
    /* Main background - Justice theme */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        color: #e0e0e0;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f1419 0%, #1a1f26 100%);
        padding: 2rem 1rem;
    }
    
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
        color: #f59e0b !important;
    }
    
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] li {
        color: #d1d5db !important;
        font-size: 0.95rem;
    }
    
    /* Title - Gold color for justice */
    h1 {
        color: #f59e0b;
        text-align: center;
        font-size: 2.5em;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    /* Chat messages */
    .user-msg {
        background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
        color: #ffffff;
        padding: 1rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        margin-left: 20%;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    
    .bot-msg {
        background: linear-gradient(135deg, #78350f 0%, #f59e0b 100%);
        color: #ffffff;
        padding: 1rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        margin-right: 20%;
        border-left: 4px solid #fbbf24;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    
    /* Input field */
    .stChatInput input {
        background-color: #1f2937 !important;
        color: #e0e0e0 !important;
        border: 2px solid #f59e0b !important;
        border-radius: 25px !important;
        padding: 12px 20px !important;
    }
    
    /* Spinner */
    .stSpinner > div {
        border-top-color: #f59e0b !important;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Initialize NyaySetu (cached)
if "nyaysetu" not in st.session_state:
    with st.spinner("Loading NyaySetu Legal Assistant..."):
        st.session_state.nyaysetu = get_nyaysetu()

# Sidebar
with st.sidebar:
    st.markdown("## About NyaySetu")
    st.markdown("### न्याय सेतु - Bridge to Justice")
    st.markdown("""
    Your AI assistant for Indian law and legal information.
    
    ### What can I help with?
    Get general information about laws, rights, legal procedures, 
    and the Indian legal system.
    
    ---
    
    ### Example Questions:
    
    **Rights & Laws:**
    - "What are fundamental rights under Indian Constitution?"
    - "What is Section 420 IPC?"
    
    **Legal Procedures:**
    - "How to file an FIR?"
    - "What is the process for divorce in India?"
    
    **Property & Business:**
    - "Property registration process in India"
    - "How to register a company?"
    
    **Consumer Rights:**
    - "What are consumer rights in India?"
    - "How to file consumer complaint?"
    
    ---
    
    **Important:** This provides general legal information only.
    For specific legal advice, always consult a qualified lawyer.
    """)

# Main title
st.markdown("<h1>⚖️ NyaySetu - न्याय सेतु</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #f59e0b; margin-top: -1.5rem;'>Your Bridge to Legal Knowledge</p>", unsafe_allow_html=True)

# Chat display area
chat_container = st.container()

# Show all chat messages
with chat_container:
    for sender, msg in st.session_state.chat_history:
        if sender == "User":
            st.markdown(
                f"<div class='user-msg'>"
                f"<strong>You:</strong><br>{msg}"
                f"</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"<div class='bot-msg'>"
                f"<strong>NyaySetu:</strong><br>{msg}"
                f"</div>",
                unsafe_allow_html=True
            )

# Input field
user_input = st.chat_input("Ask your legal question here...")

# Process input and generate response
if user_input:
    # Add user message
    st.session_state.chat_history.append(("User", user_input))
    
    with st.spinner("Analyzing your legal query..."):
        try:
            # Generate AI response
            answer = st.session_state.nyaysetu.ask(
                user_input,
                st.session_state.chat_history[:-1]
            )
            st.session_state.chat_history.append(("NyaySetu", answer))
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.session_state.chat_history.pop()  # Remove the user message on error
    
    st.rerun()
