from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from ...infrastructure.database import db

class PokemonUsuario(db.Model):
    __tablename__ = 'PokemonUsuario'
    
    IDPokemonUsuario: Mapped[int] = mapped_column(Integer, primary_key=True)
    
    IDUsuario: Mapped[int] = mapped_column(Integer, ForeignKey('Usuario.IDUsuario'), nullable=False)
    IDTipoPokemon: Mapped[int] = mapped_column(Integer, ForeignKey('TipoPokemon.IDTipoPokemon'), nullable=False)
    
    Codigo: Mapped[str] = mapped_column(String(50), nullable=False)
    ImagemUrl: Mapped[str] = mapped_column(String(255), nullable=True) 
    Nome: Mapped[str] = mapped_column(String(100), nullable=False)
    GrupoBatalha: Mapped[bool] = mapped_column(Boolean, default=False)
    Favorito: Mapped[bool] = mapped_column(Boolean, default=False)
    
    usuario = relationship('Usuario', back_populates='pokemons')
    tipo_pokemon = relationship('TipoPokemon', back_populates='pokemons_usuario')
