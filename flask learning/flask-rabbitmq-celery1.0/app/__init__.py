from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['CELERY_BROKER_URL'] = 'amqp://rabbitmq'
    app.config['CELERY_RESULT_BACKEND'] = 'redis://redis:6379/0'

    return app
