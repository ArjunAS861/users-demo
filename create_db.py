# create_db.py
from app import create_app, db

# Create app instance
app = create_app()

# Create all tables in the database
with app.app_context():
    db.create_all()