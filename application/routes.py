from application.fighter_lists import fighter_names, fighter_surnames, nick_names, martial_art, list_of_qoutes
from random import choice, randint
from application import app, db
from application.models import Fighters

@app.route('/')

@app.route('/read')
def read():
    all_profiles = Fighters.query.all()
    output = ""
    for each_profile in all_profiles:
        output += str(each_profile.name) + ' - ' + str(each_profile.art) + ' - ' + str(each_profile.wins) + ' wins ' + ' - ' + str(each_profile.qoute) + " <br> "
    return output

@app.route('/name')
def name():
    return f"{choice(fighter_names)} '{choice(nick_names)}' {choice(fighter_surnames)}"

@app.route('/art')
def art():
    return choice(martial_art)

@app.route('/profile')
def profile():
    fighter_name = name()
    martial_art = art()
    qoute = choice(list_of_qoutes)
    ko = randint(5, 10)
    sub = randint(7, 14)

    if martial_art == "Boxing":
        profile = f"{fighter_name} - {martial_art} - {ko} wins by KO - {qoute}"
        table_entry = Fighters(name = fighter_name, art = martial_art, wins = ko, qoute = qoute)
        db.session.add(table_entry)
        db.session.commit()
        return profile

    elif martial_art == "Submission Grappling":
        profile = f"{fighter_name} - {martial_art} - {sub} wins by Submission - {qoute}"
        table_entry = Fighters(name = fighter_name, art = martial_art, wins = sub, qoute = qoute)
        db.session.add(table_entry)
        db.session.commit()
        return profile

    elif martial_art == "MMA":
        profile = f"{fighter_name} - {martial_art} - {ko} wins by TKO and {sub} wins by Submission - {qoute}"
        table_entry = Fighters(name = fighter_name, art = martial_art, wins = sub+ko, qoute = qoute)
        db.session.add(table_entry)
        db.session.commit()
        return profile
        
    
    