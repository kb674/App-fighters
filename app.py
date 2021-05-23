from flask import Flask
from random import choice, randint

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "Home"

@app.route('/name')
def name():
    names = ['Paulita', 'Manna', 'Tillie', 'Lamprecht', 'Jayme', 'Fannin', 'Caleb', 'Moris', 'Sideny', 'Monte']
    surnames = ['Coombs', 'Gallows', 'Franzoni', 'Hoeppner', 'Costello', 'Scotti', 'Mellor', 'Lowenstein', 'Merino', 'Portier']
    nick_names = ["The Beast", "The Dentist", "Beauty and the Beast", "Angel of Death", "Sugar Free", "Ice Cold", "Shogun", "The Thunder", "The Dreamcatcher", "War Machine", "Was a Bullfrog", "Sick Dog", "Cheesesteak", "Cabbage", "Stinkyfeet", "The Word", "Gouda Gouda"]
    return f"{choice(names)} '{choice(nick_names)}' {choice(surnames)}"

@app.route('/art')
def art():
    martial_art = ['Boxing', 'Submission Grappling', 'MMA']
    return choice(martial_art)

@app.route('/final')
def final():
    list_of_qoutes = ['I want to outlive my children.',"This is a rat race...but I ain't no rat. I'm a turtle. A ninja turtle.", "I have gained some weight, and it is affecting my car's fuel consumption.", "My grandma's 100 years old, I am 44 years old and I am in great shape."]

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

