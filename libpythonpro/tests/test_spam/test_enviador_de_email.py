import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['sevirismo@gmail.com', 'cupcake@patisserie.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'bubbaloolunkah@gmail.com',
        'Sobre o curso PyTools',
        '''Vamos iniciar com o estudo do Pytest usando uma emulação de 
        spam para os usuários do banco de dados.'''
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'cupcakepatisserie.com.br']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'bubbaloolunkah@gmail.com',
            'Sobre o curso PyTools',
            '''Vamos iniciar com o estudo do Pytest usando uma emulação de 
            spam para os usuários do banco de dados.'''
        )

