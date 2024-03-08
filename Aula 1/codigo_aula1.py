#automação de tarefas com python
#importar o pyautogui (depois de baixar com o pip install pyautogui)
import pyautogui
import time
import pandas as pd 
#é bom baixar o pandas, numpy e openpyxl


#para pausar uma automação basta levar o mause até o canto superior esquerdo.


pyautogui.PAUSE = 0.5
#dá uma pausa de 0.5 segundos durante cada comando;


#pyautogui.click(x=valor, y=valor) -> clicar em algum lugar da tela;
#pyautogui.write -> escrever um texto;
#pyautogui.press -> pressionar 1 tecla do teclado;
#pyautogui.hotkey("ctrl", "c") -> combinação de teclas;
#pyautogui.position() -> dá a posição do mause na tela no momento da execução do código;
#retorna x e y das posições.


#entrar no sistema da empresa (pelo navegador)
#https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press('enter')
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
#variavel com o link
pyautogui.write(link)
pyautogui.press('enter')

# dar uma pausa maior
time.sleep(3)
#da uma pausa de 3 segundos no programa


#os locais dos clicks a seguir podem mudar de acordo com a resolução de cada pc. 
#rodar o seguinte código para obter a posição do mouse no pc especifico:
'''
import pyautogui
import time

time.sleep(5)
print(pyautogui.position())
'''
#colocar o mouse na posição em menos de 5 segundos

#adicionar o email e senha na pagina inicial
#add e-mail
pyautogui.click(x=1000, y=362)
pyautogui.write('mataugusto1999@gmail.com')
#add senha
pyautogui.click(x=806, y=460)
pyautogui.write('senha123')
#entrando
pyautogui.click(x=973, y=522)

#importar a base de dados
dados = pd.read_csv("produtos.csv")
print(dados)


#codigo: (x=801, y=247)
for linha in dados.index:
    #codigo
    pyautogui.click(x=801, y=247)
    pyautogui.write(dados.loc[linha, 'codigo'])

    #marca
    pyautogui.click(x=777, y=348)
    pyautogui.write(dados.loc[linha, 'marca'])

    #tipo
    pyautogui.press('tab')
    pyautogui.write(dados.loc[linha, 'tipo'])

    #categoria
    pyautogui.press('tab')
    pyautogui.write(str(dados.loc[linha, 'categoria']))

    #preco
    pyautogui.press('tab')
    pyautogui.write(str(dados.loc[linha, 'preco_unitario']))

    #custo
    pyautogui.press('tab')
    pyautogui.write(str(dados.loc[linha, 'custo']))

    #obs
    obs = dados.loc[linha, 'obs']
    pyautogui.press('tab')
    if not pd.isna(obs):
        pyautogui.write(obs)
    

    #enviando
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(5000)
    #pyautogui.press('pgup')


