import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Open AI
API = os.getenv("OPENAI_API_KEY")

# Importing

# coding

openai.api_key = API

def QuestionAnswer(question, chat_log=None):
    Filelog = open("DataBase\\qna_log.txt", "r")
    chat_log_template = Filelog.read()
    Filelog.close()

    if chat_log is None:
        chat_log = chat_log_template

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": question}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4o",  # Updated model name
        messages=messages,
        temperature=0.5,
        max_tokens=60,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0
    )
    answer = response.choices[0].message['content'].strip()
    chat_log_template_update = chat_log_template + f"\nYou : {question} \nJarvis : {answer}"
    Filelog = open("DataBase\\qna_log.txt", "w")
    Filelog.write(chat_log_template_update)
    Filelog.close()
    return answer

print(QuestionAnswer("What is the capital of India?"))

