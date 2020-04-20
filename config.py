import os
import json

basedir = os.path.abspath(os.path.dirname(__file__))

with open('config.json') as config_file:
    config = json.load(config_file)

class Config:
    SQLALCHEMY_DATABASE_URI = config.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = config.get('SECRET_KEY')
    APP_USERNAME = config.get('APP_USERNAME')
    APP_PASSWORD = config.get('APP_PASSWORD')
    CHARGE_AMOUNT_USD = 155
    STRIPE_PUBLISHABLE_KEY = config.get('STRIPE_PUBLISHABLE_KEY')
    STRIPE_SECRET_KEY = config.get('STRIPE_SECRET_KEY')
