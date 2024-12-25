from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def QuestionAnswer(question):
    try:
        messages = [
            {"role": "system", "content": "You are Jarvis, a helpful AI assistant focused on providing accurate and concise answers to questions."},
            {"role": "user", "content": question}
        ]

        response = client.chat.completions.create(
            model="gpt-4",  # Updated model name
            messages=messages,
            temperature=0.5,
            max_tokens=150
        )
        
        return response.choices[0].message.content.strip()
        
    except Exception as e:
        print(f"Error in QuestionAnswer: {str(e)}")
        return "I apologize, but I encountered an error processing your question. Please try again."
