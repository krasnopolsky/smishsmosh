

#import db_definitions

#Data endpoints for SWCCG
#Nesting these under route decorators in app.py

def testendpoint():
	print "Test worked!"

def testdb(schema):
    print schema.query.filter_by(id=0).first()

def create_deck(decks,player_deck):
    pass

