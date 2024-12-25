import streamlit as st
from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionAnswer
from Brain.VoiceHandler import speech_to_text, text_to_speech
from audio_recorder_streamlit import audio_recorder
import os
from dotenv import load_dotenv
import tempfile
from pathlib import Path

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
    .stAudioInput {
        margin: 1rem 0;
    }
    .voice-btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 0.5rem 1rem;
        background-color: #3182CE;
        color: white;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
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
        # Add audio playback for assistant messages
        if message["role"] == "assistant" and len(message["content"]) > 0:
            audio_file = text_to_speech(message["content"])
            if audio_file:
                st.audio(audio_file, format="audio/mp3")

# Voice input
st.write("🎤 Voice Input")
audio_bytes = audio_recorder()
if audio_bytes:
    # Save audio to temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as audio_file:
        audio_file.write(audio_bytes)
        audio_path = audio_file.name

    # Convert speech to text
    with st.spinner("Processing voice input..."):
        text = speech_to_text(audio_path)
        if text:
            # Add user message to chat
            st.session_state.messages.append({"role": "user", "content": text})
            with st.chat_message("user"):
                st.markdown(text)

            # Get AI response
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    try:
                        if any(keyword in text.lower() for keyword in ["what", "how", "why", "when", "where", "?"]):
                            response = QuestionAnswer(text)
                        else:
                            response = ReplyBrain(text)
                        
                        # Add assistant response to chat
                        st.session_state.messages.append({"role": "assistant", "content": response})
                        st.markdown(response)
                        
                        # Convert response to speech
                        audio_file = text_to_speech(response)
                        if audio_file:
                            st.audio(audio_file, format="audio/mp3")
                    
                    except Exception as e:
                        st.error("Sorry, I encountered an error. Please try again.")
                        print(f"Error: {str(e)}")

    # Clean up temporary file
    os.unlink(audio_path)

# Text input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                if any(keyword in prompt.lower() for keyword in ["what", "how", "why", "when", "where", "?"]):
                    response = QuestionAnswer(prompt)
                else:
                    response = ReplyBrain(prompt)
                
                # Add assistant response to chat
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.markdown(response)
                
                # Convert response to speech
                audio_file = text_to_speech(response)
                if audio_file:
                    st.audio(audio_file, format="audio/mp3")
            
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
    - 🎤 Voice input/output
    - ❓ Q&A capabilities
    - 🔊 Text-to-speech
    
    ### Tips
    - Click the microphone to use voice input
    - Responses are automatically read aloud
    - Clear chat to start fresh
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
