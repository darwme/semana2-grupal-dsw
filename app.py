from flask import Flask 
from utils.db import db
from services.predio import predio
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION
from dotenv import load_dotenv

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_CONNECTION

#SQLAlchemy(app)
db.init_app(app)
app.register_blueprint(predio)

with app.app_context():
    db.create_all

port = int(os.getenv("PORT", default="5000"))

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True, port=port)
