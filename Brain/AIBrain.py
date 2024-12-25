from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ReplyBrain(question, chat_history=None):
    try:
        messages = [
            {"role": "system", "content": "You are Jarvis, a helpful and knowledgeable AI assistant."},
            {"role": "user", "content": question}
        ]
        
        if chat_history:
            messages = chat_history + messages

        response = client.chat.completions.create(
            model="gpt-4",  # Updated model name
            messages=messages,
            temperature=0.7,
            max_tokens=150
        )
        
        return response.choices[0].message.content.strip()
        
    except Exception as e:
        print(f"Error in ReplyBrain: {str(e)}")
        return "I apologize, but I encountered an error. Please try again."
