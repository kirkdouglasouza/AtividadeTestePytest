import pytest
import requests

# BASE URL da Star Wars API
BASE_URL = "https://swapi.dev/api"

def request_and_validate(endpoint, expected_status_code=200):
    """Função auxiliar para realizar requisições e validar status code."""
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == expected_status_code, f"Erro ao acessar {endpoint}: {response.status_code}"
    return response.json()

# Testes de sucesso
def test_get_person():
    data = request_and_validate("/people/1/")
    assert data["name"] == "Luke Skywalker", f"Nome incorreto: {data['name']}"
    print(f"Personagem retornado: {data['name']}")

def test_get_movie():
    data = request_and_validate("/films/1/")
    assert data["title"] == "A New Hope", f"Título incorreto: {data['title']}"
    print(f"Filme retornado: {data['title']}")

def test_get_species():
    data = request_and_validate("/species/1/")
    assert data["name"] == "Human", f"Nome da espécie incorreto: {data['name']}"
    print(f"Espécie retornada: {data['name']}")

def test_get_planet():
    data = request_and_validate("/planets/1/")
    assert data["name"] == "Tatooine", f"Nome do planeta incorreto: {data['name']}"
    print(f"Planeta retornado: {data['name']}")

def test_get_starship():
    data = request_and_validate("/starships/9/")
    assert data["name"] == "Death Star", f"Nome da nave incorreto: {data['name']}"
    print(f"Nave retornada: {data['name']}")

# Testes de erro
def test_invalid_person():
    endpoint = "/people/9999/"  # ID inexistente
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 404, f"Esperado 404, mas retornado {response.status_code}"
    print(f"Erro retornado corretamente para {endpoint}")

def test_invalid_endpoint():
    endpoint = "/invalid_endpoint/"  # Endpoint inexistente
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 404, f"Esperado 404, mas retornado {response.status_code}"
    print(f"Erro retornado corretamente para {endpoint}")
