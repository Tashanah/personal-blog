import os

class  Config:
    QUOTES_API_BASE_URL='http://quotes.stormconsultancy.co.uk/random.json'
    QUOTES_API_KEY = os.environ.get('QUOTES_API_KEY')
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://tashanah:tash1234@localhost/blogpost'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    pass

class prodConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True 

config_options ={
    'development':DevConfig,
    'production':prodConfig
}
