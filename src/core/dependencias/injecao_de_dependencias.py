from injector import Module, provider, singleton
from src.infrastructure.repositories.usuario_repository import UsuarioRepository
from src.core.usecases.usuario.usuario_use_case import UsuarioUseCase
from src.infrastructure.clients.pokeapi_client import PokeApiClient
from src.infrastructure.repositories.pokemon_usuario_repository import PokemonUsuarioRepository
from src.infrastructure.repositories.tipo_pokemon_repository import TipoPokemonRepository
from src.core.usecases.pokemon.pokemon_use_case import PokemonUseCase

class AppModule(Module):
    @singleton
    @provider
    def provide_usuario_repository(self) -> UsuarioRepository:
        return UsuarioRepository()

    @provider
    def provide_usuario_use_case(self, repository: UsuarioRepository) -> UsuarioUseCase:
        return UsuarioUseCase(repository=repository)
    
    @provider
    def provide_pokeapi_client(self) -> PokeApiClient:
        return PokeApiClient()

    @singleton
    @provider
    def provide_pokemon_usuario_repository(self) -> PokemonUsuarioRepository:
        return PokemonUsuarioRepository()

    @provider
    def provide_pokemon_use_case(self, client: PokeApiClient, repo: PokemonUsuarioRepository) -> PokemonUseCase:
        return PokemonUseCase(pokeapi_client=client, repository=repo)
    
    @singleton
    @provider
    def provide_tipo_pokemon_repository(self) -> TipoPokemonRepository:
        return TipoPokemonRepository()
    
    @provider
    def provide_pokemon_use_case(
        self, 
        client: PokeApiClient, 
        pokemon_repo: PokemonUsuarioRepository,
        tipo_repo: TipoPokemonRepository 
    ) -> PokemonUseCase:
        return PokemonUseCase(
            pokeapi_client=client, 
            repository=pokemon_repo, 
            tipo_pokemon_repository=tipo_repo
        )