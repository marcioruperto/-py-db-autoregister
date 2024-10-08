import pyautogui
import time
import pandas as pd
# Passo 1: abrir site

pyautogui.PAUSE = 1
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
# Sistema criado apenas para testes de cadastro!

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.click(x=343, y=62)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(3)
# Passo 2: Fazer log ingalinhotricoloco
pyautogui.click(x=506, y=405)
pyautogui.write('marciruperto@email.com')
pyautogui.press('tab')
pyautogui.write('galinhotricoloco')
pyautogui.press('tab')
pyautogui.press('enter')

# Passo 3: Importar a base de dados
base_de_dados = pd.read_csv('produtos.csv')
time.sleep(3)
# Passo 4: Cadastrar produtos
for linha in base_de_dados.index:
    pyautogui.click(x=570, y=291)

    codigo = base_de_dados.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    marca = base_de_dados.loc[linha, 'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')

    tipo = base_de_dados.loc[linha, 'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    categoria = base_de_dados.loc[linha, 'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    preco_unitario = base_de_dados.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')

    custo = base_de_dados.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')
    obs = base_de_dados.loc[linha, 'obs']
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('home')
