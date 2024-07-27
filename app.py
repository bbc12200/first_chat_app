from flask import Flask, render_template
from flask_socketio import SocketIO, send
import mysql.connector


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('chat.html')  # This will be created in Step 3

# Connect to MySQL
db = mysql.connector.connect(
    host="i943okdfa47xqzpy.cbetxkdyhwsb.us-east-1.rds.amazonaws.com",
    user="sbfo9e83wgyagzj9",
    password="fo4vlinqzi7zx7iw",
    database="cmqarrutv0q65t4x"
)

@socketio.on('message')
def handleMessage(msg):
    cursor = db.cursor()
    sql = "INSERT INTO chat_history (message) VALUES (%s)"
    cursor.execute(sql, (msg,))
    db.commit()
    send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
