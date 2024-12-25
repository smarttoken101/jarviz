import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Open AI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

def ReplyBrain(question, chat_history=None):
    try:
        messages = [
            {"role": "system", "content": "You are Jarvis, a helpful and knowledgeable AI assistant."},
            {"role": "user", "content": question}
        ]
        
        # Add chat history if provided
        if chat_history:
            messages = chat_history + messages

        response = openai.ChatCompletion.create(
            model="gpt-4o",  # Updated to correct model name
            messages=messages,
            temperature=0.7,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        
        return response.choices[0].message['content'].strip()
        
    except Exception as e:
        print(f"Error in ReplyBrain: {str(e)}")
        return "I apologize, but I encountered an error. Please try again."
