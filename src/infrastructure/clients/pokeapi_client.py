import requests

class PokeApiClient:
    BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

    def get_pokemon(self, nome_pokemon: str) -> dict | None:
        """ Busca um Pokémon na PokeAPI pelo nome. """
        try:
            response = requests.get(f"{self.BASE_URL}{nome_pokemon.lower()}")
            response.raise_for_status() 
            return response.json()
        except requests.exceptions.HTTPError as err:
            if err.response.status_code == 404:
                return None 
            raise err 