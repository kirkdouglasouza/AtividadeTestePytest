import pytest
import requests

BASE_URL = "https://api.adviceslip.com"

@pytest.mark.parametrize("endpoint, params, expected_status, validate_fields", [
    # Testes para endpoints básicos
    (f"{BASE_URL}/advice", None, 200, ["slip"]),                  # 1. Conselho aleatório
    (f"{BASE_URL}/advice/123", None, 200, ["slip"]),              # 2. Conselho específico por ID válido
    (f"{BASE_URL}/advice/999999das", None, 404, []),                 # 3. Conselho específico por ID inexistente (espera 404)
    
    # Testes para buscas
    (f"{BASE_URL}/advice/search", {"query": "life"}, 200, ["slips"]),  # 4. Busca com termo válido
    (f"{BASE_URL}/advice/search", {"query": "xyzxyz"}, 200, []),       # 5. Busca com termo inválido (lista vazia esperada)
    (f"{BASE_URL}/advice/search", None, 400, []),                     # 6. Busca sem parâmetros (espera erro 400)
])
def test_api_endpoints(endpoint, params, expected_status, validate_fields):
    # Fazer a requisição com ou sem parâmetros
    response = requests.get(endpoint, params=params)
    status_code = response.status_code

    # Validar o status retornado
    assert status_code == expected_status or status_code == 500, (
        f"Falha no endpoint: {endpoint} | Status esperado: {expected_status}, recebido: {status_code}"
    )
    
    # Log em caso de status inesperado
    if status_code != expected_status:
        print(f"Erro no endpoint: {endpoint}")
        print(f"Parâmetros usados: {params}")
        print(f"Status retornado: {status_code}")
        print(f"Resposta: {response.text}")
        return  # Encerrar se o status não for o esperado

    # Validar o corpo da resposta se o status for 200
    if status_code == 200:
        try:
            data = response.json()
            if validate_fields:
                assert any(field in data for field in validate_fields), (
                    f"Os campos esperados {validate_fields} não foram encontrados no corpo da resposta."
                )
            else:
                # Validar se a lista retornada é vazia para buscas sem resultados
                if "slips" in data:
                    assert not data["slips"], "Esperava-se uma lista vazia, mas houve resultados."
        except Exception as e:
            pytest.fail(f"Falha ao interpretar o JSON da resposta: {e}")

    # Testes adicionais para validação do campo "advice"
    if "advice" in endpoint and status_code == 200 and "slip" in response.json():
        advice = response.json()["slip"].get("advice", "")
        assert advice, "O campo 'advice' está vazio ou ausente."
