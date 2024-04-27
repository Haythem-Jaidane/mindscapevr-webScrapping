from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from model.Data import db
from controller.Data import scrape
from route.Data import blueprint

app = Flask(__name__)  # flask app object
app.config.from_object('config')  # Configuring from Python Files

db.init_app(app) 

app.register_blueprint(blueprint, url_prefix='/data')

migrate = Migrate(app, db)

with app.app_context():
    scrape()


if __name__ == '__main__':
    app.run(host='192.168.137.1', port=9000, debug=True)