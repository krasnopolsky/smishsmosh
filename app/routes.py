#from gevent import monkey
#monkey.patch_all()

import random
import time
from threading import Thread
from flask import Flask, g, render_template, session, request, url_for, redirect, json, jsonify
from flask.ext.socketio import SocketIO, emit, join_room, leave_room, \
    close_room, disconnect

from app import app, socketio, db
from db_definitions import SWD








#playertest = player_info('test','test@test.com')
#db.session.add(playertest)
#db.session.commit()

#decktest = decks(insert_card_id_array_here)
#db.session.add(decktest)
#db.session.commit()

@app.route('/')
def index():
    print SWD.query.filter_by(id=0).first()
    return render_template('index.html')

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


#Write Database endpoints:

#@app.route('/create_user', methods=['POST'])
#def create_user():



@app.route('/create_deck')
def createdeck():
    swendpoints.create_deck()



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
