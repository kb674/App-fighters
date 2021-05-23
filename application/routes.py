from application.fighter_lists import fighter_names, fighter_surnames, nick_names, martial_art, list_of_qoutes
from random import choice, randint
from application import app, db
from application.models import Fighters
from flask import render_template, redirect, url_for

@app.route('/')
@app.route('/home')
def home():
    all_profiles = Fighters.query.all()
    latest_profile = Fighters.query.order_by(Fighters.id.desc()).first()
    output = ""
    return render_template("index.html", title="Home", all_profiles=all_profiles, latest_profile=latest_profile)

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
        return redirect(url_for("home"))
        

    elif martial_art == "Submission Grappling":
        profile = f"{fighter_name} - {martial_art} - {sub} wins by Submission - {qoute}"
        table_entry = Fighters(name = fighter_name, art = martial_art, wins = sub, qoute = qoute)
        db.session.add(table_entry)
        db.session.commit()
        return redirect(url_for("home"))
        

    elif martial_art == "MMA":
        profile = f"{fighter_name} - {martial_art} - {ko} wins by TKO and {sub} wins by Submission - {qoute}"
        table_entry = Fighters(name = fighter_name, art = martial_art, wins = sub+ko, qoute = qoute)
        db.session.add(table_entry)
        db.session.commit()
        return redirect(url_for("home"))
        
        
    
    