import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base config."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/excel_processor'
    # ALLOWED_EXTENSIONS = {'xlsx', 'xls', 'csv'}
    # MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size

class DevelopmentConfig(Config):
    """Development config."""
    DEBUG = True
    TESTING = False
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/excel_processor'

class ProductionConfig(Config):
    """Production config."""
    DEBUG = False
    TESTING = False
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/excel_processor_prod'
