from flask import Flask
from random import choice, randint
from fighter_lists import fighter_names, fighter_surnames, nick_names, martial_art, list_of_qoutes

app = Flask(__name__)

@app.route('/')

@app.route('/home')
def home():
    return "Home"

@app.route('/name')
def name():
    return f"{choice(fighter_names)} '{choice(nick_names)}' {choice(fighter_surnames)}"

@app.route('/art')
def art():
    return choice(martial_art)

@app.route('/four')
def four():
    fighter_name = name()
    martial_art = art()
    qoute = choice(list_of_qoutes)
    ko = randint(5, 10)
    sub = randint(7, 14)

    if martial_art == "Boxing":
        return f"{fighter_name} - {martial_art} - {ko} wins by KO - {qoute}"
    elif martial_art == "Submission Grappling":
        return f"{fighter_name} - {martial_art} - {sub} wins by Submission - {qoute}"
    elif martial_art == "MMA":
        return f"{fighter_name} - {martial_art} - {ko} wins by TKO and {sub} wins by Submission - {qoute}"

    
if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)

