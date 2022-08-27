# importando nossas bibliotecas
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

def abrir_site(url):

    # Entrar no site
    driver.get(url)

    # aguardar 5 segundos para o site abrir
    time.sleep(5)

def escolher_idioma(idioma):
    # encontrar o idioma baseado na sigla
    selecionar_idioma = driver.find_element_by_css_selector(f'#langSelect-{idioma}')
    
    # clicar no idioma escolhiddo
    selecionar_idioma.click()
    
    # aguardar 5 segundos para o site recarregar
    time.sleep(5)

def aceitar_cookies():
    # encontrar botao de aceite dos cookies
    aceitar = driver.find_element_by_css_selector('.cc_btn.cc_btn_accept_all')
    
    # clicar no botao
    aceitar.click()

def fechar_backup():
    try:
        # recuperar div onde esta a janela de backup
        div_nota = driver.find_element_by_css_selector('#note-1')
        
        # encontrar botao de fechar nota de backup
        fechar_nota_backup = div_nota.find_element_by_css_selector('.close')

        # clicar no botao
        fechar_nota_backup.click()
        
    except NoSuchElementException:
        fechar_backup()

def clicar_cookie():
    cookie = driver.find_element_by_css_selector('#bigCookie')
    while True:
        cookie.click()
        buscar_upgrade()
        buscar_powerup()

def buscar_upgrade():
    upgrade_div = driver.find_element_by_css_selector('#upgrades')
    
    upgrades_disponiveis = upgrade_div.find_elements_by_css_selector('.crate.upgrade.enabled')
    
    if(len(upgrades_disponiveis)):
        upgrades_disponiveis[0].click()

def buscar_powerup():
    powerup_div = driver.find_element_by_css_selector('#products')
    
    powerups_disponiveis = powerup_div.find_elements_by_css_selector('.product.unlocked.enabled')
    
    if(len(powerups_disponiveis)):
        powerups_disponiveis[0].click()


# Abrir o navegador
driver = webdriver.Chrome(ChromeDriverManager(log_level=0).install())

abrir_site('https://orteil.dashnet.org/cookieclicker/')

aceitar_cookies()

escolher_idioma('PT-BR')

fechar_backup()

clicar_cookie()