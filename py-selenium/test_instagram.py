from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_instagram_login():
    # Configurar o driver
    driver = webdriver.Chrome()  # Ou use o driver correspondente ao seu navegador
    driver.maximize_window()

    try:
        # Acessar a página de login do Instagram
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)  # Esperar o carregamento da página

        # Fechar o pop-up de cookies, se aparecer
        try:
            accept_cookies = driver.find_element(By.XPATH, "//button[text()='Permitir todos']")
            accept_cookies.click()
            time.sleep(2)
        except:
            print("Nenhum pop-up de cookies encontrado.")

        # Localizar o campo de e-mail/nome de usuário
        email_field = driver.find_element(By.NAME, "username")
        email_field.send_keys("emailfalso@exemplo.com")

        # Localizar o campo de senha
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys("senhaerrada123")

        # Submeter o formulário
        password_field.send_keys(Keys.RETURN)
        time.sleep(5)

        # Verificar se uma mensagem de erro é exibida (verificação única)
        try:
            error_message = driver.find_element(By.XPATH, "//p[@id='slfErrorAlert']")
            assert "senha" in error_message.text.lower() or "usuário" in error_message.text.lower(), "Mensagem de erro não apareceu como esperado."
            print("Teste passou: Mensagem de erro foi exibida corretamente.")
        except Exception as e:
            print(f"Erro esperado não encontrado: {e}")
            print("O teste falhou ou a mensagem de erro não foi exibida corretamente.")

    finally:
        # Fechar o navegador
        driver.quit()

# Executar o teste
test_instagram_login()
