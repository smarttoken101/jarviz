import streamlit as st
from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionAnswer
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Check for API key
if not os.getenv("OPENAI_API_KEY"):
    st.error("OpenAI API key not found. Please set it in your environment variables or .env file.")
    st.stop()

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
    }
    .stButton button {
        background-color: #3182CE;
        border-radius: 8px;
    }
    div[data-testid="stChatMessage"] {
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state for chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Hello! I'm Jarvis, your AI assistant. How can I help you today?"
    })

# Title
st.title("🤖 Jarvis AI Assistant")

# Chat interface
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Show typing indicator
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Determine if it's a question
                if any(keyword in prompt.lower() for keyword in ["what", "how", "why", "when", "where", "?"]):
                    response = QuestionAnswer(prompt)
                else:
                    response = ReplyBrain(prompt)
                
                # Add assistant response to chat
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.markdown(response)
            
            except Exception as e:
                st.error("Sorry, I encountered an error. Please try again.")
                print(f"Error: {str(e)}")

# Sidebar
with st.sidebar:
    st.markdown("## About Jarvis")
    st.markdown("""
    Jarvis is your AI assistant powered by OpenAI's GPT models. 
    
    ### Features
    - 💭 Natural conversation
    - ❓ Q&A capabilities
    - 🤝 Helpful responses
    
    ### Tips
    - Be specific in your questions
    - You can ask follow-up questions
    - Use clear language
    """)
    
    # Clear chat button
    if st.button("Clear Chat"):
        st.session_state.messages = [{
            "role": "assistant",
            "content": "Hello! I'm Jarvis, your AI assistant. How can I help you today?"
        }]
        st.experimental_rerun()
    
    st.markdown("---")
    st.markdown("Made with ❤️ using Streamlit")
