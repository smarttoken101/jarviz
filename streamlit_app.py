import streamlit as st
from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionAnswer
from Body.Listen import MicExecution
import speech_recognition as sr

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Page config
st.set_page_config(page_title="Jarvis AI Assistant", page_icon="🤖")

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #1E1E1E;
        color: white;
    }
    .stTextInput > div > div > input {
        background-color: #2D3748;
        color: white;
    }
    .stButton button {
        background-color: #3182CE;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.title("🤖 Jarvis AI Assistant")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Text input
text_input = st.chat_input("Type your message here...")

# Voice input button
if st.button("🎤 Voice Input"):
    with st.spinner("Listening..."):
        try:
            voice_input = MicExecution()
            if voice_input:
                st.session_state.messages.append({"role": "user", "content": voice_input})
                with st.chat_message("user"):
                    st.write(voice_input)
                
                # Get AI response
                if "what is" in voice_input or "question" in voice_input:
                    response = QuestionAnswer(voice_input)
                else:
                    response = ReplyBrain(voice_input)
                
                st.session_state.messages.append({"role": "assistant", "content": response})
                with st.chat_message("assistant"):
                    st.write(response)
        except Exception as e:
            st.error("Error processing voice input. Please try again.")

# Handle text input
if text_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": text_input})
    with st.chat_message("user"):
        st.write(text_input)
    
    # Get AI response
    if "what is" in text_input or "question" in text_input:
        response = QuestionAnswer(text_input)
    else:
        response = ReplyBrain(text_input)
    
    # Add AI response
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)
