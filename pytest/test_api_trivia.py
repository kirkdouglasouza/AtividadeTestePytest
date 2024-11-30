import pytest
import requests

# BASE URL da Trivia API
BASE_URL = "https://the-trivia-api.com/v2"

def request_and_validate(endpoint, params=None, expected_status_code=200):
    """Função auxiliar para realizar requisições e validar status code."""
    response = requests.get(BASE_URL + endpoint, params=params)
    assert response.status_code == expected_status_code, f"Erro ao acessar {endpoint}: {response.status_code}"
    return response.json()

# Testes de sucesso
def test_get_all_questions():
    data = request_and_validate("/questions", params={"limit": 5})
    assert len(data) == 5, f"Número incorreto de questões retornadas: {len(data)}"
    for question in data:
        assert "question" in question, "Uma questão não contém a chave 'question'"
    print(f"5 questões retornadas com sucesso.")

def test_questions_by_category():
    category = "science"
    data = request_and_validate("/questions", params={"categories": category, "limit": 3})
    assert len(data) == 3, f"Número incorreto de questões retornadas: {len(data)}"
    for question in data:
        assert category in question["category"], f"A questão não pertence à categoria {category}"
    print(f"3 questões retornadas na categoria {category}.")

def test_questions_by_language():
    language = "pt-br"
    data = request_and_validate("/questions", params={"languages": language, "limit": 5})
    assert len(data) == 5, f"Número incorreto de questões retornadas: {len(data)}"
    print(f"5 questões retornadas no idioma solicitado ({language}).")

# Teste de erro


def test_invalid_category():
    invalid_category = "invalid-category"
    data = request_and_validate("/questions", params={"categories": invalid_category, "limit": 3})
    # Verificar se a categoria retornada é consistente com o esperado
    for question in data:
        assert question["category"] != invalid_category, f"Uma questão pertence à categoria inválida {invalid_category}"
    print(f"API retornou perguntas, mas nenhuma pertence à categoria inválida ({invalid_category}).")
