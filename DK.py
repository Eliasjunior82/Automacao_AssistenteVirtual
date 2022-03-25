#!/usr/bin/env python
# coding: utf-8

# # Respondendo chat
# 

# In[1]:


# Bibliotecas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import pyperclip
import pytesseract
import cv2

# Gerardor de cpf
driver = webdriver.Chrome()
driver.get('https://www.geradordecpf.org/')
driver.find_element_by_id('btn-gerar-cpf').click()
time.sleep(3)
cpf = driver.find_element_by_id('numero')
valor = cpf.get_attribute('value')

# Assistente virtual
driver = webdriver.Chrome()
driver.get('http://homol.def.assistentevirtual.sp.gov.br/')

#Fluxo Não
time.sleep(3)
driver.find_element_by_xpath('//*[@id="chats-column-holder"]/figure/div[1]').click()
nome = driver.find_element_by_id('textInput')
nome.send_keys('junior' + Keys.RETURN)
time.sleep(3)
resposta = driver.find_element_by_xpath('//*[@id="textInput"]')
resposta.send_keys('Não' + Keys.RETURN)
time.sleep(3)
resposta2 = driver.find_element_by_id('textInput')
resposta2.send_keys('Não' + Keys.RETURN)
time.sleep(3)
resposta3 = driver.find_element_by_id('textInput')
resposta3.send_keys('Não' + Keys.RETURN)
time.sleep(3)
resposta4 = driver.find_element_by_id('textInput')
resposta4.send_keys('Não' + Keys.RETURN)
time.sleep(3)
resposta5 = driver.find_element_by_id('textInput')
resposta5.send_keys('Não' + Keys.RETURN)
time.sleep(3)

#bloco Civil e Familia
resposta6 = driver.find_element_by_id('textInput')
resposta6.send_keys('Civel e familia' + Keys.RETURN)
time.sleep(3)

# Cadastro
driver.find_element_by_xpath('//*[@id="scrollingChatsd"]/div[26]/div/div/p/div/div[1]').click()
time.sleep(3)
resposta7 = driver.find_element_by_id('textInput')
resposta7.send_keys('Maria da silva' + Keys.RETURN)
time.sleep(3)
resposta8 = driver.find_element_by_id('textInput')
resposta8.send_keys(valor + Keys.RETURN)
time.sleep(3)
resposta9 = driver.find_element_by_id('textInput')
resposta9.send_keys('33.822.978-0' + Keys.RETURN)
time.sleep(3)
resposta10 = driver.find_element_by_id('textInput')
resposta10.send_keys('03978340' + Keys.RETURN)
time.sleep(3)
resposta11 = driver.find_element_by_id('textInput')
resposta11.send_keys('67' + Keys.RETURN)
time.sleep(3)
resposta12 = driver.find_element_by_id('textInput')
resposta12.send_keys('(11)99999-3456' + Keys.RETURN)
time.sleep(3)
resposta12 = driver.find_element_by_id('textInput')
resposta12.send_keys('texte@gmail.com' + Keys.RETURN)
time.sleep(3)
resposta13 = driver.find_element_by_id('textInput')
resposta13.send_keys('08/05/1985' + Keys.RETURN)
time.sleep(3)
resposta14 = driver.find_element_by_id('textInput')
resposta14.send_keys('Josefina da Silva' + Keys.RETURN)
time.sleep(3)
decisao = driver.find_element_by_xpath('//*[@id="scrollingChatsd"]/div[47]/div/div/p')
time.sleep(3)
#######
#pyautogui.hotkey('Alt', 'Tab' )
time.sleep(2)
pyautogui.press('win')
time.sleep(1)
pyautogui.write('ferramenta de captura')
time.sleep(1)
pyautogui.press('enter')
time.sleep(3)
pyautogui.click(970,169)
pyautogui.click(451,196)
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(274,70)
time.sleep(3)
pyautogui.press('Delete')
time.sleep(2)
pyautogui.write('captura_de_cpf')
time.sleep(1)
pyautogui.click(525,499)
time.sleep(3)

#############

# ler imagem
imagem = cv2.imread('captura_de_cpf.PNG')

caminho = r'C:\Program Files\Tesseract-OCR'
#extrair imagem
pytesseract.pytesseract.tesseract_cmd = caminho + r'\tesseract.exe'
texto = pytesseract.image_to_string(imagem)

print(texto)

# Transformando Texto da foto em lista
final = texto.split()


# Validando cpf
cpff = final[25]
print(cpff)
print(valor)
if cpff == valor:
    print('CPF valido')
else:
    print('CPF Divergente')
    
       
# excluido o arquivo da pasta

time.sleep(2)
pyautogui.click(555, 749)
time.sleep(1)
pyautogui.click(282, 242)
time.sleep(3)
pyautogui.click(1081, 157)
time.sleep(1)
pyautogui.write('captura_de_cpf')
time.sleep(1)
pyautogui.press('Enter')
time.sleep(1)
pyautogui.click(269,200)
time.sleep(1)
pyautogui.press('Enter')
time.sleep(2)
pyautogui.click(661,54)
time.sleep(1)
pyautogui.click(1342, 13)
time.sleep(1)
pyautogui.click(1342, 13)






