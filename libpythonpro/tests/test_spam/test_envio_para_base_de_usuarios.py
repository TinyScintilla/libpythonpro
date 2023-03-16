from unittest.mock import Mock

import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Raiene', email='bubbaloolunkah@gmail.com'),
            Usuario(nome='Rosa', email='cupcakepatisserie.com.br')
        ],
        [
            Usuario(nome='Raiene', email='bubbaloolunkah@gmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'bubbaloolunkah@gmail.com',
        'Curso Pytools',
        'Confira a lib Pytest'
    )
    assert len(usuarios) == enviador.enviar.call_count



def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Raiene', email='bubbaloolunkah@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'rosa-maria@gmail.com',
        'Curso Pytools',
        'Confira a lib Pytest'
    )
    enviador.enviar.assert_called_once_with (
        'rosa-maria@gmail.com',
        'bubbaloolunkah@gmail.com',
        'Curso Pytools',
        'Confira a lib Pytest'
    )