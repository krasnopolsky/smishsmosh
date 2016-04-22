#from gevent import monkey
#monkey.patch_all()

import random
import time
import json
import uuid
from threading import Thread
from flask import Flask, g, render_template, session, request, url_for, redirect, json, jsonify
from flask.ext.socketio import SocketIO, emit, join_room, leave_room, \
    close_room, disconnect
from flask.ext.wtf import Form 
from flask.ext.login import login_user, logout_user, login_required, current_user
from wtforms import TextField, PasswordField, validators

from app import app, socketio, db, login_manager, bcrypt
from db_definitions import SWD, decks, games, player_info, player_decks, player_games, player_game_deck,  Users

@login_manager.user_loader
def user_loader(user_id):
    return Users.query.get(user_id)

class LoginForm(Form):
    username = TextField('Username', [validators.Required()])
    password = PasswordField('Password', [validators.Required()])






@app.route('/')
def index():
    print SWD.query.filter_by(id=0).first()
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():

        user = Users.query.filter_by(email=(form.username.data)).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                print user.player_id
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user)
                return redirect(url_for('get_player_decks'))
    return render_template("login.html", form=form)

@app.route('/logout')
@login_required
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    form = LoginForm()
    return render_template("login.html",form=form)

@app.route('/game_engine')
def engine():
	return render_template('indexSave.html')

@app.route('/rooms', methods=['POST'])
def rooms():
	deck = []
	decknames = []
	deck = createdeck()
	cardnames = (SWD.query.filter(SWD.id.in_(deck)).all())
	for x in cardnames:
		print x.id
		decknames.append(x.CardName)
	return render_template('socket.html', decknames=decknames)




@app.route('/create_deck', methods=['POST'])
def createdeck():

        data = request.get_json()

        new_deck = decks(data['deck_array'])
        db.session.add(new_deck)
        db.session.commit()

        new_player_deck = player_decks(data['player_id'],new_deck.deck_id)
        db.session.add(new_player_deck)
        db.session.commit()

        data_view = str((new_deck.deck_id,new_player_deck.player_id,new_player_deck.deck_id))
        return data_view


@app.route('/get_player_decks', methods=['GET','POST'])
@login_required
def get_player_decks():  
    deck_array = (player_decks.query.filter_by(player_id=current_user.player_id).all())
    player_deck_ids = []
    for deck in deck_array:
        player_deck_ids.append(deck.deck_id)
    return render_template('deckSelection.html', player_deck_ids=player_deck_ids)

#Going with a unique game ID approach, but keeping this around in case I want to use it later.
@app.route('/present_lobbies', methods=['GET', 'POST'])
@login_required
def present_lobbies():
    #render available lobbies (emit lobby information to all players, and then start games)
    return render_template('lobbies.html')

@app.route('/start_game', methods=['GET', 'POST'])
@login_required
def start_game():
    
    selected_deck = request.form["selected_deck"]
    is_light = 1 #data['is_light']
    
    game_id = str(uuid.uuid4())[:8]
    
    if is_light:
        new_game = player_games(game_id, current_user.player_id, None)
    else: 
        new_game = player_games(game_id, None, current_user.player_id)

    db.session.add(new_game)
    db.session.commit()

    game_deck = player_game_deck(game_id, current_user.player_id, selected_deck)

    db.session.add(game_deck)
    db.session.commit()

    return redirect(url_for('load_game', game_id=game_id)) 


@app.route('/game/<game_id>')
def load_game(game_id):

    return render_template('game_engine.html', game_id=game_id)


@app.route('/join_game', methods = ["GET","POST"])
def join_game():

    selected_deck = request.form["selected_deck"]
    selected_game_id = request.form["selected_game_id"]

    target_game = player_games.query.filter_by(game_id=selected_game_id).first()
    
    if target_game:
        if target_game.light_player_id:
            target_game.dark_player_id = current_user.player_id
        else:
            target_game.light_player_id = current_user.player_id
        
        db.session.commit()
        

        return redirect(url_for('load_game', game_id=target_game.game_id)) 

    else:
        return "No Game Found!"

    #accept game_id, add in some validations, and add player to existing game in db
    pass

@app.route('/draw_card', methods=['GET', 'POST'])
def draw_card():
    cardID = request.form['randCard']
    print cardID
    card = (SWD.query.filter_by(id=cardID).first())
    return jsonify(abbreviation = card.Abbreviation,
 ability = card.Ability,
 armor = card.Armor,
 astromech = card.Astromech,
 cancels = card.Cancels,
 cardname = card.CardName,
 cardnamev = card.CardNameV,
 cardtype = card.CardType,
 characteristics = card.Characteristics,
 combo = card.Combo,
 counterpart = card.Counterpart,
 creature = card.Creature,
 creaturedefensevalue = card.CreatureDefenseValue,
 creaturedefensevaluename = card.CreatureDefenseValueName,
 darksideicons = card.DarkSideIcons,
 darksidetext = card.DarkSideText,
 deploy = card.Deploy,
 destiny = card.Destiny,
 droid = card.Droid,
 episode1 = card.Episode1,
 errata = card.Errata,
 expansion = card.Expansion,
 expansionv = card.ExpansionV,
 exterior = card.Exterior,
 ferocity = card.Ferocity,
 forceaptitude = card.ForceAptitude,
 forfeit = card.Forfeit,
 gametext = card.Gametext,
 grabber = card.Grabber,
 grouping = card.Grouping,
 hyperspeed = card.Hyperspeed,
 icons = card.Icons,
 independent = card.Independent,
 influence = card.Influence,
 information = card.Information,
 interior = card.Interior,
 inventory = card.Inventory,
 iscanceledby = card.IsCanceledBy,
 ispulled = card.IsPulled,
 jeditestnumber = card.JediTestNumber,
 landspeed = card.Landspeed,
 lightsideicons = card.LightSideIcons,
 lightsidetext = card.LightSideText,
 lore = card.Lore,
 maneuver = card.Maneuver,
 matching = card.Matching,
 matchingweapon = card.MatchingWeapon,
 mobile = card.Mobile,
 modeltype = card.ModelType,
 needs = card.Needs,
 objectiveback = card.ObjectiveBack,
 objectivebackname = card.ObjectiveBackName,
 objectivefront = card.ObjectiveFront,
 objectivefrontname = card.ObjectiveFrontName,
 parsec = card.Parsec,
 permanentweapon = card.PermanentWeapon,
 pilot = card.Pilot,
 planet = card.Planet,
 politics = card.Politics,
 power = card.Power,
 pulls = card.Pulls,
 rarity = card.Rarity,
 republic = card.Republic,
 rules = card.Rules,
 scomplink = card.ScompLink,
 selectivecreature = card.SelectiveCreature,
 space = card.Space,
 starship = card.Starship,
 subtype = card.Subtype,
 tradefederation = card.TradeFederation,
 underground = card.Underground,
 underwater = card.Underwater,
 uniqueness = card.Uniqueness,
 uniquenessv = card.UniquenessV,
 vehicle = card.Vehicle,
 warrior = card.Warrior,
 id = card.id)





@socketio.on('lobby', namespace='/lobby')
def lobby_selected(lobby):
    print lobby
    pass

@socketio.on('message', namespace='/test')
def message_test(data):
    print data
    emit('response', data, namespace='/test', broadcast=True)


@socketio.on('my event', namespace='/test')
def test_message(randCard):
    cardID = randCard['randCard']
    print cardID
    card = (SWD.query.filter_by(id=cardID).first())
    emit('my response', {'abbreviation': card.Abbreviation,
 'ability': card.Ability,
 'armor': card.Armor,
 'astromech': card.Astromech,
 'cancels': card.Cancels,
 'cardname': card.CardName,
 'cardnamev': card.CardNameV,
 'cardtype': card.CardType,
 'characteristics': card.Characteristics,
 'combo': card.Combo,
 'counterpart': card.Counterpart,
 'creature': card.Creature,
 'creaturedefensevalue': card.CreatureDefenseValue,
 'creaturedefensevaluename': card.CreatureDefenseValueName,
 'darksideicons': card.DarkSideIcons,
 'darksidetext': card.DarkSideText,
 'deploy': card.Deploy,
 'destiny': card.Destiny,
 'droid': card.Droid,
 'episode1': card.Episode1,
 'errata': card.Errata,
 'expansion': card.Expansion,
 'expansionv': card.ExpansionV,
 'exterior': card.Exterior,
 'ferocity': card.Ferocity,
 'forceaptitude': card.ForceAptitude,
 'forfeit': card.Forfeit,
 'gametext': card.Gametext,
 'grabber': card.Grabber,
 'grouping': card.Grouping,
 'hyperspeed': card.Hyperspeed,
 'icons': card.Icons,
 'independent': card.Independent,
 'influence': card.Influence,
 'information': card.Information,
 'interior': card.Interior,
 'inventory': card.Inventory,
 'iscanceledby': card.IsCanceledBy,
 'ispulled': card.IsPulled,
 'jeditestnumber': card.JediTestNumber,
 'landspeed': card.Landspeed,
 'lightsideicons': card.LightSideIcons,
 'lightsidetext': card.LightSideText,
 'lore': card.Lore,
 'maneuver': card.Maneuver,
 'matching': card.Matching,
 'matchingweapon': card.MatchingWeapon,
 'mobile': card.Mobile,
 'modeltype': card.ModelType,
 'needs': card.Needs,
 'objectiveback': card.ObjectiveBack,
 'objectivebackname': card.ObjectiveBackName,
 'objectivefront': card.ObjectiveFront,
 'objectivefrontname': card.ObjectiveFrontName,
 'parsec': card.Parsec,
 'permanentweapon': card.PermanentWeapon,
 'pilot': card.Pilot,
 'planet': card.Planet,
 'politics': card.Politics,
 'power': card.Power,
 'pulls': card.Pulls,
 'rarity': card.Rarity,
 'republic': card.Republic,
 'rules': card.Rules,
 'scomplink': card.ScompLink,
 'selectivecreature': card.SelectiveCreature,
 'space': card.Space,
 'starship': card.Starship,
 'subtype': card.Subtype,
 'tradefederation': card.TradeFederation,
 'underground': card.Underground,
 'underwater': card.Underwater,
 'uniqueness': card.Uniqueness,
 'uniquenessv': card.UniquenessV,
 'vehicle': card.Vehicle,
 'warrior': card.Warrior,
 'id': card.id})
    



if __name__ == '__main__':
    socketio.run(app)
