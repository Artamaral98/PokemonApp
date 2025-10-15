from src.core.entities import Usuario
from src.infrastructure.repositories.usuario_repository import UsuarioRepository
from passlib.hash import pbkdf2_sha256 as cryp
from src.core.exceptions.user_exeption import UsuarioJaExistenteException, CredenciaisInvalidasException
from flask_jwt_extended import create_access_token

class UsuarioUseCase:
    def __init__(self, repository: UsuarioRepository):
        self._repository = repository

    def registrar_usuario(self, nome, login, email, senha):
        usuario_existe = self._repository.get_usuario_por_email_ou_login(email, login)
        
        if usuario_existe:
            raise UsuarioJaExistenteException("Já existe um usuário com este e-mail ou login.")

        senha_hash = cryp.hash(senha)
        novo_usuario = Usuario(Nome=nome, Login=login, Email=email, Senha=senha_hash)
        
        return self._repository.add_usuario(novo_usuario)

    def login(self, login, senha):
        user = self._repository.get_usuario_por_login(login)

        if not user or not cryp.verify(senha, user.Senha):
            raise CredenciaisInvalidasException("Login ou senha inválidos.")

        access_token = create_access_token(identity=user.IDUsuario)
        return access_token