from flask import Flask, request
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_injector import FlaskInjector
from injector import Injector
from src.infrastructure.database import db
from src.config import Config
from src.core.dependencias.injecao_de_dependencias import AppModule
from src.api.routes.auth_routes import auth_bp
from src.api.routes.pokemon_routes import pokemon_bp
from src.core.exceptions.jwt_error_handler import register_jwt_error_handlers


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)
    jwt = JWTManager(app)
    register_jwt_error_handlers(jwt)

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(pokemon_bp, url_prefix='/api/pokemon')

    injector = Injector([AppModule()])
    FlaskInjector(app=app, injector=injector)

    with app.app_context():
        from src.core import entities 
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)