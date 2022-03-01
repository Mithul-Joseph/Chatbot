#importing libraries
import openai
from flask import Flask, render_template, request

app = Flask(__name__)
openai.api_key = 'YOUR_OPENAI_API_KEY'

#giving a start prompt for the model.
starter_prompt = """"The following is a friendly conversation between a human and an AI assistant. 
The AI assistant is very intelligent, helpful, friendly, empathetic, energetic.
Human: Hello friend
AI: Hi there. Its nice to meet you.
Human: How are you?
AI: I'm good thankyou. How are you doing?"""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def bot_response():

    userText = request.args.get('msg')
    text = add_prompt(userText)
    response = openai.Completion.create(
    engine="text-davinci-001",
    prompt=text,
    temperature=0.6,
    max_tokens = 50
    )
    global starter_prompt
    starter_prompt+=response.choices[0].text
    return str(response.choices[0].text)

def add_prompt(userText):
    global starter_prompt
    starter_prompt+="\nHu: "+userText+"\nAI: "
    return starter_prompt

if __name__ == "__main__":
    app.run(debug = False, host = '0.0.0.0', port=8080)