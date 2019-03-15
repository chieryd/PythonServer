from sqlalchemy.dialects import postgresql
from sqlalchemy import FLOAT
from app import db

class NodeModel(db.Model):
    __tablename__ = 'nodes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), index=True, unique=True)
    subtitle = db.Column(db.String(300), index=True, unique=True)
    image = db.Column(db.String(100), index=True, unique=True)
    transform = db.Column(postgresql.ARRAY(FLOAT))
    type = db.Column(db.Integer, index=True, unique=True)

