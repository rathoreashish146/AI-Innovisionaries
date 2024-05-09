from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings,chunks,chatbot


from dotenv import load_dotenv
from src.prompt import *
import os
import openai

app = Flask(__name__)

load_dotenv()


@app.route("/")
def index():
    return render_template('chat.html') 



@app.route("/get", methods=["GET", "POST"])
def chat():
    chat_history=[]
    msg = request.form["msg"]
    input = msg
    print(input)
    result,chat_history=chatbot(input,chat_history)
    print(chat_history)
    print("Response : ", result)
    return str(result)



if __name__ == '__main__':
    app.run(host='localhost',port=8080,debug=True)