# Jarvis AI Assistant

A modern AI chatbot with web interface, built using Streamlit and OpenAI.

## Features
- 🤖 GPT-powered responses
- 💬 Chat interface
- ❓ Q&A mode
- 🌐 Web-based access

## Setup
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file with your OpenAI API key:
```
OPENAI_API_KEY=your_key_here
```

3. Run the app:
```bash
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