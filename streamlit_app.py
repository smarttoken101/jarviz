import streamlit as st
from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionAnswer
from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(
    page_title="Jarvis AI Assistant",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        max-width: 800px;
        margin: 0 auto;
    }
    .stTextInput > div > div > input {
        background-color: #2D3748;
        color: white;
    }
    .stButton button {
        background-color: #3182CE;
        color: white;
        border-radius: 8px;
    }
    .user-message {
        background-color: #3182CE;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
    .assistant-message {
        background-color: #2D3748;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Title
st.title("🤖 Jarvis AI Assistant")
st.markdown("---")

# Chat interface
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
prompt = st.chat_input("Type your message here...")

if prompt:
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Get AI response
    with st.spinner("Thinking..."):
        try:
            if any(keyword in prompt.lower() for keyword in ["what is", "how to", "explain", "?"]):
                response = QuestionAnswer(prompt)
            else:
                response = ReplyBrain(prompt)
            
            # Add assistant response to chat
            st.session_state.messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.write(response)
        
        except Exception as e:
            st.error("Sorry, I encountered an error. Please try again.")
            print(f"Error: {str(e)}")

# Add information about the app
with st.sidebar:
    st.markdown("## About Jarvis")
    st.markdown("""
    Jarvis is your AI assistant powered by OpenAI's GPT models. 
    
    Features:
    - 💭 Chat naturally
    - ❓ Ask questions
    - 🤝 Get helpful responses
    """)
    
    st.markdown("---")
    st.markdown("Made with ❤️ using Streamlit")
