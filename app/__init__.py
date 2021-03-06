from flask import Flask, Blueprint
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restplus import Api
from flask_qrcode import QRcode

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
QRcode(app)

api = Api(app, 
    version='0.8.1',
    title="Switch API", 
    description="Switch services API listing.", 
    default='General',
    doc=False
    )

from app import routes, farer, events, models, reg, addons, payments, attend
