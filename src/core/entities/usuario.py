from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from ...infrastructure.database import db

class Usuario(db.Model):
    __tablename__ = 'Usuario'
    
    IDUsuario: Mapped[int] = mapped_column(Integer, primary_key=True)
    Nome: Mapped[str] = mapped_column(String(100), nullable=False)
    Login: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    Email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    Senha: Mapped[str] = mapped_column(String(255), nullable=False)
    DtInclusao: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    DtAlteracao: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    pokemons = relationship('PokemonUsuario', back_populates='usuario')