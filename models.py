import sqlalchemy as db
from datetime import datetime
from database import metadata



categories = db.Table('categories', metadata,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('name', db.String, unique=True, nullable=False)
)

expenses = db.Table('expenses', metadata,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('description', db.String),
    db.Column('amount', db.Float, nullable=False),
    db.Column('category_id', db.Integer , db.ForeignKey('categories.id'), nullable=False),
    db.Column('date', db.DateTime, default=datetime.utcnow)
    
)

budgets = db.Table('budgets', metadata,
                   
    db.Column('id' , db.Integer, primary_key=True),
    db.Column('year_month', db.String , unique=True , nullable=False),
    db.Column('amount', db.Float , nullable=False)
    
)