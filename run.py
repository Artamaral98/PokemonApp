from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from src.infrastructure.database import db
from src.config import Config
def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)
    JWTManager(app)

    with app.app_context():
        from src.core import entities 
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)