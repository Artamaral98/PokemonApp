from src.core.entities import PokemonUsuario
from src.infrastructure.database import db

class PokemonUsuarioRepository:
    def add(self, pokemon_usuario: PokemonUsuario):
        db.session.add(pokemon_usuario)
        db.session.commit()
        return pokemon_usuario