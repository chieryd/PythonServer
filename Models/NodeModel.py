from app import db

class NodeModel(db.Model):
    __tablename__ = 'nodes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    subtitle = db.Column(db.String(300))
    image = db.Column(db.String(100))
    transform = db.Column(db.String(500))
    nodetype = db.Column(db.Integer)

