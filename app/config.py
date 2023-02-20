import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    """Base Config Object"""
    DEBUG = True

    ## all data below is taked from .env file from the root of the directory

    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')  ## secret key, will default to Som3$ec5etK*y
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'localhost')    ## mail server address, default to localhost
    MAIL_PORT = os.environ.get('MAIL_PORT', '25')       ## mail port default to 25
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')     ## mail username will be used from .env   
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')     ## mail password will be used from .env  