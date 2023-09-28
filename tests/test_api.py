import requests
import pytest


ENDPOINT = 'https://cl2u.ru/'


def test_connect_api():
    connect_response = connect()
    assert connect_response.status_code == 200


@pytest.mark.django_db
def test_create_url():
    payload = create_payload()
    create_url_response = create_url(payload)
    assert create_url_response.status_code == 200
    data = create_url_response.json()
    print(data)


@pytest.mark.django_db
def test_redirect_count():
    payload = create_payload()
    create_url_response = create_url(payload)
    assert create_url_response.status_code == 200
    data = create_url_response.json()
    response = requests.get(data['short_link'])



def connect():
    return requests.get(ENDPOINT)


def create_url(payload):
    return requests.post(ENDPOINT + 'url', json=payload)


def get_url(short_url):
    return requests.get(ENDPOINT + f'{short_url}')


def create_payload():
    url = 'https://www.honeybadger.io/blog/django-test-github-actions/1'
    return {
        'url': url,
    }


def get_payload():
    url = 'https://www.honeybadger.io/blog/django-test-github-actions/'
    return {
        'url': url,
        'short_url': '1a9e2d'
    }
