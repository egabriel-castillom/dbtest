import mysql.connector
from flask import g,Flask
import os
from dotenv import load_dotenv

load_dotenv()

def get_db(): 
    g.db = mysql.connector.connect(
        host = os.environ.get('FLASK_DATABASE_HOST'),
        user = os.environ.get('FLASK_DATABASE_USER'),
        password = os.environ.get('FLASK_DATABASE_PASSWORD'),
        database = os.environ.get('FLASK_DATABASE')
    )
    g.c = g.db.cursor(dictionary=True)
    return g.db,g.c

app = Flask(__name__)

@app.route('/', methods =['GET'])
def muestrainfo():
    db,c = get_db()
    c.execute('SELECT * FROM email')
    result = c.fetchall()
    return result

if __name__ == "__main__":
    app.run()


