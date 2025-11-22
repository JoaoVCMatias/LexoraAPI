from .usuario import router as usuario_router
from .domino import router as dominio_router
from .validacao import router as validacao_router
from .questao import router as questao_router

__all__ = ["usuario_router", "dominio_router", "validacao_router", "questao_router"]

