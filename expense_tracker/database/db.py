import sqlalchemy as db
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
load_dotenv()

DB_URL = os.getenv('DB_URL', 'sqlite:///expenses.db')
engine = create_engine(DB_URL,echo=False)
metadata = db.MetaData()

def setup_database():
    metadata.create_all(engine)