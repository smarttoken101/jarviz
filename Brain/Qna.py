import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

def QuestionAnswer(question):
    try:
        messages = [
            {"role": "system", "content": "You are Jarvis, a helpful AI assistant focused on providing accurate and concise answers to questions."},
            {"role": "user", "content": question}
        ]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.5,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        
        return response.choices[0].message['content'].strip()
        
    except Exception as e:
        print(f"Error in QuestionAnswer: {str(e)}")
        return "I apologize, but I encountered an error processing your question. Please try again."
