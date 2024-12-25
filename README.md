# Jarvis AI Assistant

A modern AI chatbot with web interface, built using Streamlit and OpenAI.

## Features
- 🤖 GPT-powered responses
- 💬 Chat interface
- ❓ Q&A mode
- 🌐 Web-based access

## Setup

### Windows
```bash
# Create and activate virtual environment
setup.bat

# Run the app
venv\Scripts\streamlit run streamlit_app.py
```

### Unix/Linux/Mac
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run streamlit_app.py
```

## Deployment
1. Push to GitHub
2. Deploy on [Streamlit Cloud](https://streamlit.io/cloud)
3. Set environment variables in Streamlit Cloud settings

## Structure

- `streamlit_app.py`: Main application file
- `Brain/`: AI processing modules
- `Body/`: Voice input/output modules

## License

MIT License