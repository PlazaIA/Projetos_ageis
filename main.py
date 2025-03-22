import os
from Login import linkedin_login, acessar_pagina_empregos  # Importando funções do login

# Pegando credenciais do .env
from dotenv import load_dotenv
load_dotenv()
EMAIL = os.getenv("LINKEDIN_EMAIL")
PASSWORD = os.getenv("LINKEDIN_PASSWORD")

# Executa o login
driver = linkedin_login(EMAIL, PASSWORD)

if driver:
    acessar_pagina_empregos(driver)