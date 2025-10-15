from src.core.entities import Usuario
from src.infrastructure.database import db
from sqlalchemy import or_

class UsuarioRepository:
    def add_usuario(self, usuario: Usuario):
        db.session.add(usuario)
        db.session.commit()
        return usuario

    def get_usuario_por_email(self, email: str) -> Usuario | None:
        return Usuario.query.filter_by(Email=email).first()
    
    def get_usuario_por_email_ou_login(self, email: str, login: str) -> Usuario | None:
        return Usuario.query.filter(
            or_(Usuario.Email == email, Usuario.Login == login)
        ).first()
    
    def get_usuario_por_login(self, login: str) -> Usuario | None:
        return Usuario.query.filter_by(Login=login).first()