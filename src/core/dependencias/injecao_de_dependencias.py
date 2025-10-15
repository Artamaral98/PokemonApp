from injector import Module, provider, singleton
from src.infrastructure.repositories.usuario_repository import UsuarioRepository
from src.core.usecases.usuario.usuario_use_case import UsuarioUseCase

class AppModule(Module):
    @singleton
    @provider
    def provide_usuario_repository(self) -> UsuarioRepository:
        return UsuarioRepository()

    @provider
    def provide_usuario_use_case(self, repository: UsuarioRepository) -> UsuarioUseCase:
        return UsuarioUseCase(repository=repository)