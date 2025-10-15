from src.infrastructure.clients.pokeapi_client import PokeApiClient
from src.infrastructure.repositories.pokemon_usuario_repository import PokemonUsuarioRepository
from src.infrastructure.repositories.tipo_pokemon_repository import TipoPokemonRepository
from src.core.entities import PokemonUsuario, TipoPokemon
from src.core.exceptions.pokemons_exceptions import PokemonNaoEncontradoException


class PokemonUseCase:
    def __init__(
        self, 
        pokeapi_client: PokeApiClient, 
        repository: PokemonUsuarioRepository,
        tipo_pokemon_repository: TipoPokemonRepository):
        self._pokeapi_client = pokeapi_client
        self._repository = repository
        self._tipo_pokemon_repo = tipo_pokemon_repository

    def favoritar_pokemon(self, id_usuario: int, nome_pokemon: str):
        pokemon_data = self._pokeapi_client.get_pokemon(nome_pokemon)
        if not pokemon_data:
            raise PokemonNaoEncontradoException(f"Pokémon '{nome_pokemon}' não encontrado.")
        
        tipos_pokemon_api = pokemon_data.get('types', [])
        if not tipos_pokemon_api:
            tipo_principal = 'normal'
        else:
            tipo_principal = tipos_pokemon_api[0]['type']['name']
        
        tipo_obj = self.obter_ou_criar_tipo_pokemon(tipo_principal)

        novo_favorito = PokemonUsuario(
            IDUsuario=id_usuario,
            Codigo=str(pokemon_data['id']),
            Nome=pokemon_data['name'].capitalize(),
            ImagemUrl=pokemon_data['sprites']['front_default'],
            Favorito=True,
            GrupoBatalha=False,
            IDTipoPokemon=tipo_obj.IDTipoPokemon
        )
        
        return self._repository.add(novo_favorito)
        
    def obter_ou_criar_tipo_pokemon(self, nome_tipo: str) -> TipoPokemon:
        tipo_db = self._tipo_pokemon_repo.get_by_descricao(nome_tipo)
        if not tipo_db:
            novo_tipo = TipoPokemon(Descricao=nome_tipo)
            tipo_db = self._tipo_pokemon_repo.add(novo_tipo)
        return tipo_db

