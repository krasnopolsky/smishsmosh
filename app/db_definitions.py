from app import db




#Copy of db definitions in app.py TO DO: create a model directory for these and remove them from app.py
class Users(db.Model):
    __table__ = db.Model.metadata.tables['Users']

    def __init__(self,email,password):
        self.email = email
        self.password = password

    def is_active(self):
        return True

    def get_id(self):
        return self.player_id

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False

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



class player_decks(db.Model):
    __table__ = db.Model.metadata.tables['player_decks']

    def __init__(self,player_id,deck_id):
        self.player_id = player_id
        self.deck_id = deck_id

class player_games(db.Model):
    __table__ = db.Model.metadata.tables['player_games']

    def __init__(self,game_id,light_player_id,dark_player_id):
        self.game_id = game_id
        self.light_player_id = light_player_id
        self.dark_player_id = dark_player_id

