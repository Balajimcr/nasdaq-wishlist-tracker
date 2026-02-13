"""
Configuration file for NASDAQ Wishlist Tracker
"""
import os

class Config:
    """Base configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    NGROK_AUTH_TOKEN = os.environ.get('NGROK_AUTH_TOKEN') or ''

    # App settings
    FLASK_PORT = 5000
    DEBUG = False

    # Default watchlist
    DEFAULT_WATCHLIST = [
        "AAPL", "MSFT", "NVDA", "GOOGL", "AMZN", 
        "TSLA", "META", "NFLX", "AMD", "INTC"
    ]

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False

# Config dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
