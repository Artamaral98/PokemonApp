from src.core.entities import TipoPokemon
from src.infrastructure.database import db

class TipoPokemonRepository:
    def get_by_descricao(self, descricao: str) -> TipoPokemon | None:
        return TipoPokemon.query.filter_by(Descricao=descricao).first()

    def add(self, tipo_pokemon: TipoPokemon) -> TipoPokemon:
        db.session.add(tipo_pokemon)
        db.session.commit()
        return tipo_pokemon