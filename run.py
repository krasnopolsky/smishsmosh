from app import app
from app import socketio
#app.run(debug=True) have to use socketio run method to enable sockets
socketio.run(app)
