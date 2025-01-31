from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
from app.config import Config

mongo = PyMongo()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    CORS(app)
    mongo.init_app(app)
    
    # Register blueprints
    from app.routes import api
    app.register_blueprint(api)
    
    return app
