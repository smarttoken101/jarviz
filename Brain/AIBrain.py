import openai
from dotenv import load_dotenv
import os
from pathlib import Path

# Load environment variables
load_dotenv()

# Open AI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Ensure DataBase directory exists
database_dir = Path("DataBase")
database_dir.mkdir(exist_ok=True)

# Initialize chat log file if it doesn't exist
chat_log_file = database_dir / "chat_log.txt"
if not chat_log_file.exists():
    chat_log_file.write_text("", encoding="utf-8")

def ReplyBrain(question, chat_log=None):
    try:
        # Read existing chat log
        chat_log_template = chat_log_file.read_text(encoding="utf-8")
        
        if chat_log is None:
            chat_log = chat_log_template

        messages = [
            {"role": "system", "content": "You are Jarvis, a helpful and knowledgeable AI assistant."},
            {"role": "user", "content": question}
        ]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Using a valid model name
            messages=messages,
            temperature=0.7,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        
        answer = response.choices[0].message['content'].strip()
        
        # Update chat log
        chat_log_template_update = chat_log_template + f"\nUser: {question}\nJarvis: {answer}\n"
        chat_log_file.write_text(chat_log_template_update, encoding="utf-8")
        
        return answer
        
    except Exception as e:
        print(f"Error in ReplyBrain: {str(e)}")
        return "I apologize, but I encountered an error. Please try again."
