import pandas as pd
import plotly.express as px
import pyautogui
import pyperclip
import Analisar

Analisar()

#enviando esses graficos por email e wats
email = input("Digite o email desejado: ")
contato = input("Digite o nome desejado: ")
mensagem = """
Olá;
Segue abaixo os gráficos das análises de dados:
"""

#pause de segundos entre as tarefas
pyautogui.PAUSE = 10

#abrir uma nova guia no navegador
pyautogui.click(x=2020, y=13)

#abrindo o gmail
pyperclip.copy("www.gmail.com")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")

#clicar no botao escrever
pyautogui.click(x=1511, y=174)

#digitar os dados do email
pyperclip.copy(email)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

pyperclip.copy("Gráficos das análises de dados")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

#pegando as paginas html
#abrir o clips
pyautogui.click(x=2789, y=1003)
#abrir os projetos
pyautogui.click(x=2917, y=939)
#pesquisar os projetos
pyautogui.click(x=1737, y=62)
pyperclip.copy(r"C:\Users\adrya\Documents\Python\Python curso 4\Análise de Dados")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")
pyautogui.click(x=1603, y=417)
pyperclip.copy("Grafico-tamanho.zip")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")

pyautogui.click(x=2671, y=998)
print("E-mail enviado com sucesso")

#-------------------------------------------------------------------#
#ENVIO POR WHATSAPP AGORA
#clicando no icone do wats
pyautogui.click(x=1386, y=193)
pyautogui.click(x=1546, y=111)
pyperclip.copy(contato)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")

#enviando mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")

#procurando arquivo
pyautogui.click(x=1928, y=998)
#acessando documentos
pyautogui.click(x=1920, y=738)
pyautogui.click(x=2085, y=665)
pyautogui.click(x=1775, y=63)
pyperclip.copy(r"C:\Users\adrya\Documents\Python\Python curso 4\Análise de Dados")
pyautogui.hotkey("ctrl", "v")

pyautogui.click(x=1623, y=418)
pyperclip.copy("Grafico-tamanho.zip")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")
pyautogui.click(x=2469, y=978)

print("Mensagem enviada com sucesso")
