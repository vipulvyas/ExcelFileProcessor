from app import create_app
from app.config import Config, DevelopmentConfig, ProductionConfig
from flask import Flask
from flask_cors import CORS
import os

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    
    # Load configuration based on environment
    app.config.from_object(config_class)
    
    # Enable CORS
    CORS(app)
    
    # Register blueprints
    from app.routes import api
    app.register_blueprint(api)
    
    return app

# Use environment variable to determine configuration
config = ProductionConfig if os.environ.get('FLASK_ENV') == 'production' else DevelopmentConfig
app = create_app(config)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 2000)),
        debug=app.config['DEBUG']
    )
