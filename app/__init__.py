from flask import Flask, request, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api


app = Flask(__name__)
app.config.from_object('config')
api_bp = Blueprint('api', __name__)

# 这里会import出去
api = Api(api_bp)

app.register_blueprint(api_bp, url_prefix='/api')

# 数据库关联
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes

from Models.NodeModel import NodeModel