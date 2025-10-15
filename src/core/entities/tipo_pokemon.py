from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from ...infrastructure.database import db

class TipoPokemon(db.Model):
    __tablename__ = 'TipoPokemon'
    
    IDTipoPokemon: Mapped[int] = mapped_column(Integer, primary_key=True)
    Descricao: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    pokemons_usuario = relationship('PokemonUsuario', back_populates='tipo_pokemon')