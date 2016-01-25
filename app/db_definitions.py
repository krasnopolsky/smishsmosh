from app import db



#Copy of db definitions in app.py TO DO: create a model directory for these and remove them from app.py

class decks(db.Model):
    __table__ = db.Model.metadata.tables['decks']

    def __init__(self,card_array):
        cardnum = 0
        for card_id in card_array:
            cardnum += 1
            setattr(self,"deck_card_%d" % cardnum, card_id)


class games(db.Model):
    __table__ = db.Model.metadata.tables['games']

    def __init__(self,game_id):
        self.game_id = game_id

class player_info(db.Model):
    __table__ = db.Model.metadata.tables['player_info']

    def __init__(self,email,password):
        self.email = email
        self.password = password


class SWD(db.Model):
	__table__ = db.Model.metadata.tables['SWD']

