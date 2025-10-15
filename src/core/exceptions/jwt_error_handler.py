from flask import jsonify, Blueprint
from flask_jwt_extended import JWTManager 
from src.core.schemas.api_response_dto import ApiResponseDTO

def register_jwt_error_handlers(jwt: JWTManager):
    """
    Registra os tratadores de erro customizados para o Flask-JWT-Extended.
    """
    
    @jwt.unauthorized_loader
    def unauthorized_callback(reason):
        response_dto = ApiResponseDTO(success=False, message="Acesso negado. É necessário um token de autorização.")
        return jsonify(response_dto.model_dump()), 401

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        response_dto = ApiResponseDTO(success=False, message="Token de autorização inválido")
        return jsonify(response_dto.model_dump()), 401

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        response_dto = ApiResponseDTO(success=False, message="Seu token de acesso expirou. Por favor, faça login novamente.")
        return jsonify(response_dto.model_dump()), 401