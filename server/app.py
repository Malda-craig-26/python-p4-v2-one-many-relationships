# server/app.py
#!/usr/bin/env python3

from flask import Flask
from flask_migrate import Migrate
from models import db, Employee, Onboarding, Review

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

# ✅ First initialize the db
db.init_app(app)

# ✅ Then set up Flask-Migrate
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(port=5555, debug=True)
