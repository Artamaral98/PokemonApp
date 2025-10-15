from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.core.usecases.pokemon.pokemon_use_case import PokemonUseCase
from src.core.schemas.pokemon_schemas import FavoritePayload
from src.core.schemas.api_response_dto import ApiResponseDTO 

pokemon_bp = Blueprint('pokemon', __name__)

@pokemon_bp.route('/favorite', methods=['POST'])
@jwt_required()
def favoritar_pokemon(use_case: PokemonUseCase):
    """
    Endpoint para um usuário logado favoritar um Pokémon.
    """
    payload = FavoritePayload(**request.get_json())
    
    id_usuario_logado = get_jwt_identity()

    novo_favorito = use_case.favoritar_pokemon(
        id_usuario=id_usuario_logado,
        nome_pokemon=payload.nome_pokemon
    )

    response = ApiResponseDTO(
        success=True,
        message=f"Pokémon '{novo_favorito.Nome}' adicionado aos favoritos."
    )
    return jsonify(response.model_dump()), 201