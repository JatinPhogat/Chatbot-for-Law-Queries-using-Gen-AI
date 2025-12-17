# ⚖️ NyaySetu (न्याय सेतु) - AI Legal Assistant

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.40.0-FF4B4B.svg)](https://streamlit.io)
[![LangChain](https://img.shields.io/badge/LangChain-0.3.25-green.svg)](https://langchain.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Bridge to Justice** - An intelligent AI-powered legal assistant that provides information about Indian laws, legal procedures, and rights using Retrieval-Augmented Generation (RAG) technology.

https://github.com/user-attachments/assets/520de33c-6afa-4f36-b249-e6aea61ceb7e

##  Key Features

- **Intelligent Legal Q&A**: Get accurate answers to legal questions using advanced AI
- **RAG-Powered Responses**: Retrieves information from actual legal documents (Constitution, IPC, Evidence Act, Contract Act)
- **Conversational Interface**: Natural, user-friendly chat experience with memory
- **Bilingual Support**: Works with both English and Hindi queries
- **Fast & Efficient**: Powered by Groq's Llama 3.3 70B for lightning-fast responses
- **Privacy-Focused**: Local embeddings using HuggingFace models
- **Responsive Design**: Beautiful dark-themed UI optimized for all devices

##  Use Cases

- Understanding fundamental rights and legal procedures
- Learning about specific IPC sections and laws
- Getting guidance on filing FIRs, consumer complaints, etc.
- Understanding property, marriage, and business laws
- Quick legal information for students and researchers

##  Technical Architecture

```
User Query → Streamlit UI → LangChain RAG Pipeline
                                    ↓
                          Vector Database (ChromaDB)
                                    ↓
                          Semantic Search (Top-K)
                                    ↓
                          Context + Query → Groq LLM
                                    ↓
                          Response Generation
```

**Tech Stack:**
- **Frontend**: Streamlit (Interactive Web UI)
- **LLM**: Groq API (Llama 3.3 70B Versatile)
- **Embeddings**: HuggingFace Sentence Transformers (all-MiniLM-L6-v2)
- **Vector Database**: ChromaDB
- **Framework**: LangChain (RAG Implementation)
- **Document Processing**: PyPDF

##  Prerequisites

- Python 3.10 or higher
- Windows/Linux/MacOS
- 4GB+ RAM (for local embeddings)
- Internet connection (for LLM API calls)
- Groq API Key ([Get free key](https://console.groq.com))

##  Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/JatinPhogat/Chatbot-for-Law-Queries-using-Gen-AI.git
cd Chatbot-for-Law-Queries-using-Gen-AI
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv ven
.\ven\Scripts\Activate.ps1

# Linux/Mac
python3 -m venv ven
source ven/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
```

**Get your Groq API key**: Visit [Groq Console](https://console.groq.com) and sign up for a free account.

### 5. Prepare Legal Documents
Place your PDF legal documents in the `data/` folder. The project includes:
- Constitution of India
- Indian Penal Code (IPC)
- Indian Contract Act, 1872
- Indian Evidence Act

### 6. Create Vector Embeddings
```bash
python create_embeddings.py
```
*This process takes 5-10 minutes and creates a searchable vector database from your documents.*

### 7. Run the Application
```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`

##  Project Structure

```
Nyaysetu/
│
├── app.py                      # Streamlit UI application
├── nyaysetu.py                 # Core RAG logic and AI assistant
├── create_embeddings.py        # Vector database creation script
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (create this)
├── .gitignore                  # Git ignore rules
│
├── data/                       # Legal PDF documents
│   ├── Constitution of India.pdf
│   ├── Indian Penal Code (IPC).pdf
│   ├── Indian Contract Act, 1872.pdf
│   └── Indian Evidence Act.pdf
│
└── legal_vector_store/         # Generated vector database (after setup)
```

##  Usage Examples

**Query**: *"What is Section 420 IPC?"*

**NyaySetu Response**: 
> Section 420 of the Indian Penal Code (IPC) deals with cheating and dishonestly inducing delivery of property. It states that anyone who cheats and thereby dishonestly induces the person deceived to deliver any property... [full explanation]

**Query**: *"How to file an FIR?"*

**NyaySetu Response**:
> To file an FIR (First Information Report) in India, you can visit the nearest police station and provide details of the cognizable offense. The police are obligated to register the FIR... [detailed steps]

##  Configuration

### Customize LLM Settings
Edit `nyaysetu.py` to change:
```python
# Change model
model_name="llama-3.3-70b-versatile"

# Adjust retrieval
search_kwargs={"k": 4}  # Number of relevant docs to retrieve

# Modify chunk size
chunk_size=1000
chunk_overlap=200
```

### Customize UI Theme
Edit `app.py` to modify colors and styling in the CSS section.

##  Testing

Example test queries:
- "What are fundamental rights?"
- "What is dowry prohibition act?"
- "How to register property in India?"
- "Consumer rights in India"
- "शादी के लिए कानूनी उम्र क्या है?" (Hindi)

##  Troubleshooting

### Virtual Environment Issues
If activation fails after renaming the folder:
```bash
# Delete old environment
Remove-Item -Recurse -Force ven

# Create fresh environment
python -m venv ven
.\ven\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Embeddings Creation Fails
Ensure you have:
- Stable internet connection (downloads model ~90MB)
- Sufficient RAM (4GB+)
- PDF files in `data/` folder

### Import Errors
```bash
# Reinstall with exact versions
pip install -r requirements.txt --force-reinstall
```

##  Performance Metrics

- **Response Time**: ~2-3 seconds per query
- **Document Coverage**: 2300+ legal text chunks indexed
- **Accuracy**: RAG-based responses grounded in actual legal documents
- **Concurrent Users**: Supports multiple simultaneous users

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

##  Future Enhancements

- [ ] Add more legal documents (Tax laws, Labor laws, etc.)
- [ ] Implement multilingual support (Tamil, Telugu, Bengali)
- [ ] Add voice input/output capabilities
- [ ] Deploy on cloud (AWS)
- [ ] Add user authentication and history
- [ ] Integrate case law database

##  Disclaimer

**Important**: NyaySetu provides general legal information only and is not a substitute for professional legal advice. The responses are AI-generated based on available legal documents. For specific legal matters, always consult a qualified lawyer.

##  Developer

**Jatin Phogat**
- GitHub: [@JatinPhogat](https://github.com/JatinPhogat)
- LinkedIn: [Connect with me](https://www.linkedin.com/in/jatin-phogat)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

##  Acknowledgments

- **LangChain** for the RAG framework
- **Groq** for providing fast LLM inference
- **HuggingFace** for open-source embeddings
- **Streamlit** for the amazing web framework
- **Government of India** for making legal documents publicly accessible

---

<div align="center">

**⚖️ Built with ❤️ to make legal information accessible to everyone**

[![GitHub stars](https://img.shields.io/github/stars/JatinPhogat/Chatbot-for-Law-Queries-using-Gen-AI.svg?style=social&label=Star)](https://github.com/JatinPhogat/Chatbot-for-Law-Queries-using-Gen-AI)
[![GitHub forks](https://img.shields.io/github/forks/JatinPhogat/Chatbot-for-Law-Queries-using-Gen-AI.svg?style=social&label=Fork)](https://github.com/JatinPhogat/Chatbot-for-Law-Queries-using-Gen-AI/fork)

</div>
