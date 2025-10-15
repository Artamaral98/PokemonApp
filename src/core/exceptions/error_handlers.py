from flask import jsonify, Blueprint
from pydantic import ValidationError
from src.core.schemas.usuarios_schemas import ApiResponseDTO
import traceback

from src.core.exceptions.user_exeption import (UsuarioJaExistenteException, CredenciaisInvalidasException, ErroDeValidacaoException)

def register_error_handlers(bp: Blueprint):
    """
    Registra os tratadores de erro para um determinado Blueprint.

    """
    
    @bp.errorhandler(ErroDeValidacaoException)
    def handle_error_de_validacao(error: ErroDeValidacaoException):
        response = ApiResponseDTO(
            success=False, 
            message="Erro de validação no payload.",
            errors=error.errors()
        )
        return jsonify(response.model_dump()), 422

    @bp.errorhandler(UsuarioJaExistenteException)
    def handle_usuario_existente(error: UsuarioJaExistenteException):
        response = ApiResponseDTO(success=False, message=str(error))
        return jsonify(response.model_dump()), 409

    @bp.errorhandler(CredenciaisInvalidasException)
    def handle_credenciais_invalidas(error: CredenciaisInvalidasException):
        response = ApiResponseDTO(success=False, message=str(error))
        return jsonify(response.model_dump()), 401

    # @bp.errorhandler(Exception)
    # def handle_erro_generico(error: Exception):
    #     return jsonify({"error": "Ocorreu um erro inesperado no servidor."}), 500
    
    @bp.errorhandler(Exception)
    def handle_generic_exception(error: Exception):
        traceback.print_exc()
        response = ApiResponseDTO(success=False, message="Ocorreu um erro inesperado no servidor.")
        return jsonify(response.model_dump()), 500