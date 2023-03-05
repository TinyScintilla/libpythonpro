import requests

def buscar_avatar(id):
    '''
    Busca o avatar de uma usuário no Github.
    :param usuario: str com o nome do usuário
    :return: str com o link do avatar
    '''

    url = f'https://avatars.githubusercontent.com/u/{id}?v=4'
    resp = requests.get(url)
    print('resp', resp.json()["avatar_url"])


buscar_avatar('62080076')
