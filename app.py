from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")

@ask.launch

def app_init():
    return question(
        "Variable Text Input started. " +
        "What is your Command?")

@ask.intent(
    "VariableIntent",
    mapping={"message": "Query"})

def handle_freeform(message):
    return statement(
        "Your message was: " +
        message)

if __name__ == '__main__':
    app.run()

