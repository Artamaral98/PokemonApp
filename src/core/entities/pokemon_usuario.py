from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from ...infrastructure.database import db

class PokemonUsuario(db.Model):
    __tablename__ = 'PokemonUsuario'
    
    IDPokemonUsuario: Mapped[int] = mapped_column(Integer, primary_key=True)
    
    # Chaves Estrangeiras
    IDUsuario: Mapped[int] = mapped_column(Integer, ForeignKey('Usuario.IDUsuario'), nullable=False)
    IDTipoPokemon: Mapped[int] = mapped_column(Integer, ForeignKey('TipoPokemon.IDTipoPokemon'), nullable=False)
    
    # Propriedades do Pokémon conforme o diagrama
    Codigo: Mapped[str] = mapped_column(String(50), nullable=False)
    ImagemUrl: Mapped[str] = mapped_column(String(255), nullable=True) # Pode ser nulo se não encontrado
    Nome: Mapped[str] = mapped_column(String(100), nullable=False)
    GrupoBatalha: Mapped[bool] = mapped_column(Boolean, default=False)
    Favorito: Mapped[bool] = mapped_column(Boolean, default=False)
    
    # Definição dos relacionamentos para navegação via ORM
    usuario = relationship('Usuario', back_populates='pokemons')
    tipo_pokemon = relationship('TipoPokemon', back_populates='pokemons_usuario')
