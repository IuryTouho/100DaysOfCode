# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

configs = webdriver.ChromeOptions()
configs.add_experimental_option("detach", True)

navegador = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=configs)

navegador.get("https://www.google.com/")

navegador.find_element('xpath','//*[@id="APjFqb"]').send_keys("Digimon")
navegador.find_element('xpath','//*[@id="APjFqb"]').send_keys(Keys.RETURN)

navegador.find_element('xpath','//*[@id="hdtb-sc"]/div/div/div[1]/div[2]/a/div').click()
