from unittest.mock import Mock

import pytest

from libpythonpro import github_API

@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/62080076?v=4'
    resp_mock.json.return_value = {
        'login': 'R-Lemos-prog',
        'id': 62080076,
        'avatar_url': url
    }
    get_mock = mocker.path('libpythonpro/github_API.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_API.buscar_avatar('R-Lemos-prog')
    return avatar_url == url

def test_buscar_avatar_integracao():
    url = github_API.buscar_avatar('R-Lemos-prog')
    return 'https://avatars.githubusercontent.com/u/62080076?v=4' == url