from flask import Blueprint, request, jsonify
from src.core.schemas.usuarios_schemas import RegisterPayload, LoginPayload, UserResponseDTO, ApiResponseDTO
from src.core.exceptions.error_handlers import register_error_handlers
from src.core.usecases.usuario.usuario_use_case import UsuarioUseCase


auth_bp = Blueprint('auth', __name__)

register_error_handlers(auth_bp)

@auth_bp.route('/register', methods=['POST'])
def registrar_usuario(use_case: UsuarioUseCase):
    payload = RegisterPayload(**request.get_json())
    
    novo_usuario = use_case.registrar_usuario(
        nome=payload.nome,
        login=payload.login,
        email=payload.email,
        senha=payload.senha
    )
    
    user_dto = UserResponseDTO.model_validate(novo_usuario)
    
    response_dto = ApiResponseDTO(
        success=True,
        message="Usuário criado com sucesso",
        data=user_dto
    )
    
    return jsonify(response_dto.model_dump()), 201

@auth_bp.route('/login', methods=['POST'])
def login(use_case: UsuarioUseCase):
    payload = LoginPayload(**request.get_json())
    
    access_token = use_case.login(
        login=payload.login,
        senha=payload.senha
    )

    return jsonify(access_token=access_token), 200