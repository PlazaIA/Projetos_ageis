import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

# Pegando credenciais do .env
EMAIL = os.getenv("LINKEDIN_EMAIL")
PASSWORD = os.getenv("LINKEDIN_PASSWORD")

# Configurando o ChromeDriver
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Se quiser rodar sem abrir o navegador, descomente essa linha
chrome_service = Service("/caminho/para/chromedriver")  # Coloque o caminho correto do seu ChromeDriver

def linkedin_login(email, password):
    """ Faz login no LinkedIn e mantém a página aberta no Chrome. """
    
    if not email or not password:
        print("❌ ERRO: Credenciais não encontradas! Defina as variáveis no .env.")
        return None

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    try:
        driver.get("https://www.linkedin.com/login")
        time.sleep(2)

        # Insere email
        email_input = driver.find_element(By.ID, "username")
        email_input.send_keys(email)

        # Insere senha
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys(password)
        password_input.submit()

        time.sleep(3)

        # Verifica se o login foi bem-sucedido
        if "feed" in driver.current_url:
            print("✅ Login bem-sucedido! Navegador permanecerá aberto.")
        else:
            print("❌ Falha no login. Verifique suas credenciais.")
            driver.quit()
            return None

    except Exception as e:
        print(f"Erro durante o login: {e}")
        driver.quit()
        return None

    return driver

def acessar_pagina_empregos(driver):
    """ Após login, acessa a página de empregos do LinkedIn. """
    try:
        driver.get("https://www.linkedin.com/jobs/")
        time.sleep(3)  # Espera carregar
        print("✅ Página de empregos acessada com sucesso!")
    except Exception as e:
        print(f"Erro ao acessar página de empregos: {e}")

def busca_dado_estatico(driver):
    """ Busca e retorna um nome de perfil estático na página atual """
    try:
        time.sleep(3)  # Aguarda carregamento
        
        # Tenta encontrar um nome na página (ajuste a classe correta se necessário)
        nome_element = driver.find_element(By.CLASS_NAME, "profile-card-name") 
        
        print("✅ Nome encontrado:", nome_element.text)
        return nome_element.text

    except Exception as e: 
        print(f"❌ Erro ao buscar nome: {e}")
        return None

# Executa o login
driver = linkedin_login(EMAIL, PASSWORD)

if driver:
    acessar_pagina_empregos(driver)
    busca_dado_estatico(driver)
