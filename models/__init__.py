# Tabelas independentes
from .sexo import Sexo
from .disponibilidade import Disponibilidade
from .idioma import Idioma
from .objetivo import Objetivo
from .tipo_questao import TipoQuestao
from .experiencia_idioma import ExperienciaIdioma
from .palavra import Palavra
# Tabelas dependentes
from .usuario import Usuario
from .objetivo_usuario import ObjetivoUsuario
from .questao import Questao
from .conjunto_questao import ConjuntoQuestao
from .questao_usuario import QuestaoUsuario
from .data_acesso import DataAcesso
from .email_confirmacao import EmailConfirmacao
from .experiencia_idioma_usuario import ExperienciaIdiomaUsuario
from .usuario_token import UsuarioToken
from .palavra_objetivo import PalavreObjetivo
