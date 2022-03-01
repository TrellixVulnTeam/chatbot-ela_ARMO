from flask import Flask,render_template,request
# Creating Flask app
app = Flask(__name__)

# Training ChatBot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
chatbot = ChatBot("Ela",logic_adapters=['chatterbot.logic.BestMatch','chatterbot.logic.TimeLogicAdapter','chatterbot.logic.MathematicalEvaluation'])
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english.ai","chatterbot.corpus.english.computers","chatterbot.corpus.english.botprofile","chatterbot.corpus.english.conversations","chatterbot.corpus.english.emotion","chatterbot.corpus.english.greetings","chatterbot.corpus.english.science","chatterbot.corpus.english.literature")

# Creating home page
@app.route('/')
def home():
    return render_template('index.html')
# Creating response
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    if userText == "💖":
        return str("Thanks")
    return str(chatbot.get_response(userText))

# Runing app
if __name__ == "__main__":
    app.run(debug=True)