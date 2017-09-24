from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "You are at the home page right now, fam"

@app.route("/hey")
def hey():
    return "Hey, how are you?"

@app.route("/whatsUp")
def whats_up():
    return "Ay yo what up dawg!"

if __name__ == "__main__":
    app.run()
