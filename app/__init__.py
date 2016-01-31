import os
import sys
import random
import time
from threading import Thread
from flask import Flask, render_template, session, request, url_for, redirect, json, jsonify
from flask.ext.socketio import SocketIO, emit, join_room, leave_room, \
    close_room, disconnect
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
import swendpoints

app = Flask(__name__)
app.debug = True
#app.config.from_object('config')
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://bkrasnopolsky@localhost/hothdb' #'mysql://chirpa:chewbacca5@hothDB.blandmo.com/hothdb'
socketio = SocketIO(app)
login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)
thread = None


db.Model.metadata.reflect(db.engine)



from app import routes
