from flask import Flask, render_template, request, jsonify
from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionAnswer
from Body.Listen import MicExecution
from Body.Speak import Speak

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_text', methods=['POST'])
def process_text():
    data = request.json
    user_message = data.get('message', '')
    
    if "what is" in user_message or "question" in user_message or "answer" in user_message:
        response = QuestionAnswer(user_message)
    else:
        response = ReplyBrain(user_message)
    
    return jsonify({"response": response})

@app.route('/process_voice', methods=['POST'])
def process_voice():
    voice_input = MicExecution()
    voice_input = str(voice_input).replace(".", "")
    
    if "what is" in voice_input or "question" in voice_input or "answer" in voice_input:
        response = QuestionAnswer(voice_input)
    else:
        response = ReplyBrain(voice_input)
        
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
