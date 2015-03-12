from gevent import monkey
monkey.patch_all()

import random
import time
from threading import Thread
from flask import Flask, render_template, session, request, url_for, redirect
from flask.ext.socketio import SocketIO, emit, join_room, leave_room, \
    close_room, disconnect
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://chirpa:chewbacca5@hothDB.blandmo.com/hothdb'
db = SQLAlchemy(app)
socketio = SocketIO(app)
thread = None


db.Model.metadata.reflect(db.engine)

class SWD(db.Model):
	__table__ = db.Model.metadata.tables['SWD']

cardtest = SWD.query.filter_by(id=0).first()
 

@app.route('/')
def index():
    return render_template('index.html')

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


def createdeck():
	deck = []
	for i in range(60):
		x = random.randint(1,3445)
		deck.append(x)
	return deck




@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': cardtest.CardName, 'count': 0})

@socketio.on('my event', namespace='/test')
def connect(message):
	emit('my response', {'data': message['data']})



if __name__ == '__main__':
    socketio.run(app)