import pytest
import requests

# BASE URL da API Fixer e CHAVE DA API
BASE_URL = "http://data.fixer.io/api/"
API_KEY = "6bd54dcfbe23f60c1e5fd8ee255a7b98" # CHAVE DE DA API

def test_latest_exchange_rates():
    # Teste básico: obter as taxas de câmbio mais recentes
    endpoint = "latest"
    params = {"access_key": API_KEY}
    response = requests.get(BASE_URL + endpoint, params=params)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert data["success"], f"Erro na resposta: {data.get('error')}"
    assert "rates" in data, "Taxas de câmbio não retornadas"
    print(f"Taxas de câmbio disponíveis: {len(data['rates'])}")

def test_convert_currency_with_manual_calculation():
    # Obter as taxas de câmbio mais recentes e calcular a conversão manualmente
    endpoint = "latest"
    params = {"access_key": API_KEY}
    response = requests.get(BASE_URL + endpoint, params=params)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert data["success"], f"Erro ao acessar taxas de câmbio: {data.get('error')}"
    
    rates = data["rates"]
    assert "USD" in rates and "EUR" in rates, "As taxas para USD ou EUR não foram retornadas"
    
    # Cálculo manual da conversão
    usd_to_eur_rate = rates["EUR"] / rates["USD"]
    amount_in_usd = 100
    converted_amount = amount_in_usd * usd_to_eur_rate
    
    print(f"Conversão manual de 100 USD para EUR: {converted_amount}")
    assert converted_amount > 0, "A conversão não produziu um valor válido"

def test_historical_data():
    # Buscar taxas de câmbio históricas
    endpoint = "2022-01-01"
    params = {"access_key": API_KEY}
    response = requests.get(BASE_URL + endpoint, params=params)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert data["success"], f"Erro na resposta: {data.get('error')}"
    assert "rates" in data, "Taxas de câmbio históricas não retornadas"
    print(f"Taxas de câmbio em 2022-01-01: {len(data['rates'])}")

def test_invalid_api_key():
    # Testar acesso com chave inválida
    endpoint = "latest"
    params = {"access_key": "INVALID_KEY"}
    response = requests.get(BASE_URL + endpoint, params=params)
    assert response.status_code == 200, "Erro na resposta da API"
    data = response.json()
    assert not data["success"], "A resposta deveria indicar erro"
    assert "error" in data, "Erro não retornado"
    print("Teste de chave inválida bem-sucedido")

def test_symbols_list():
    # Obter a lista de moedas suportadas
    endpoint = "symbols"
    params = {"access_key": API_KEY}
    response = requests.get(BASE_URL + endpoint, params=params)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert data["success"], f"Erro na resposta: {data.get('error')}"
    assert "symbols" in data, "Lista de moedas não retornada"
    print(f"Moedas disponíveis: {len(data['symbols'])}")
