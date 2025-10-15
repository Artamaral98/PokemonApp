class UsuarioJaExistenteException(Exception):
    """Lançada quando se tenta criar um usuário que já existe."""
    pass

class ErroDeValidacaoException(Exception):
    """Lançada quando o payload da requisição é inválido ou incompleto."""
    pass

class CredenciaisInvalidasException(Exception):
    """Lançada quando as credenciais de login são inválidas."""
    pass