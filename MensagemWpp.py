import pandas as pd 

contatos_df = pd.read_excel("Enviar.xlsx")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib
import datetime

def save_screenshot(num_screenshots):
    # Loop para tirar várias capturas de tela
    for i in range(num_screenshots):
        # Gera um nome de arquivo com base no título da página
        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{navegador.title}_{current_time}_{i+1}.png".replace(" ", "_")
        navegador.save_screenshot(filename)

# Inicializa o navegador
navegador = webdriver.Chrome('C:\Tools\chromedriver.exe')
navegador.get("https://web.whatsapp.com/")
save_screenshot(1)
time.sleep(30)

# Localiza elemento na tela depois de qr lido, para garantir que está logado
if navegador.find_element("xpath", '//*[@id="side"]/div[1]/div/div/div[1]').is_displayed():
    time.sleep(2)
    save_screenshot(1)
else:
    navegador.find_element("xpath", '//*[@id="pane-side"]/div/div[1]').is_displayed() 
    time.sleep(2)
    save_screenshot(1)

# Já estamos com o login feito no whatsapp web podemos enviar as mensagens
for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, "Pessoa"]
    numero = contatos_df.loc[i, "Número"]
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    time.sleep(10)
    navegador.find_element("xpath", '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p').send_keys(Keys.ENTER)
    save_screenshot(1)
    time.sleep(10)

# Encerra o navegador
save_screenshot(1)
navegador.quit()

#Doc de apoio para escrever, clicar e definir elementos e for para tirar print da tela.

# Novos jeito de clicar e escreve em um campo usando selenium

#driver.find_element("xpath",'//*[@id="APjFqb"]').click
#driver.find_element("xpath",'//*[@id="APjFqb"]').send_keys("teste")

# Define o número de capturas de tela que deseja salvar
#num_screenshots = 5

# Loop para tirar as capturas de tela
#for i in range(num_screenshots):
# Salva a captura de tela com um nome único
#screenshot_name = f"image_{i}.png"
#navegador.save_screenshot(screenshot_name)