from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

#-----------------инициализация библиотеки для firefox-------------
from selenium.webdriver.firefox.options import Options
#-----------------инициализация библиотеки для firefox-------------
#-----------------Использование Jenkins в headless режиме (без графического интерфейса)----------------
options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)
#-----------------Использование Jenkins в headless режиме (без графического интерфейса)----------------

link = "http://qa228.karpin74.beget.tech/"
# browser = webdriver.Firefox() #----отключили для запуска теста для jenkins вне графического интерфейса-----
browser.maximize_window()
browser.get(link)

mag = browser.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div[2]/nav/div[1]/ul/li[1]/a").click() #Переход во вкладку "Магазин"
mag2 = browser.find_element(By.CSS_SELECTOR, "#st-primary-content > div.woocommerce.columns-4 > ul > li:nth-child(2) > a").click() #Выбор категории "Все товары"
mag3 = browser.find_element(By.XPATH, "/html/body/div/div[3]/div/div/div/div/ul/li[1]/div/div/div[2]/div[1]/h3/a").click() #Выбор товара "Будильники"
quantity = browser.find_element(By.XPATH, "//div[@id='product-36']/div[2]/form/div/input").clear() # Очистка значения по умолчанию
quantity = browser.find_element(By.XPATH, "//div[@id='product-36']/div[2]/form/div/input").send_keys("5") # Указание количесва товаров
product = browser.find_element(By.XPATH, "//*[@id='product-36']/div[2]/form/button").click() # Клик на кнопку "В корзину"
product = browser.find_element(By.CSS_SELECTOR, "#main-header6 > div.navigation-wrapper > div.navigation-middle > div > div > div > div > div.main-menu-right.col-lg-4 > ul > li.cart-wrapper > div.cart-main > button").click() #Открытие модального окна корзины
time.sleep(2)
product = browser.find_element(By.XPATH, "/html/body/div/header/div[2]/div[1]/div/div/div/div/div[3]/ul/li[1]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]").click() #Переход по вкладке "Посмотреть корзину"

#Проверка полученных результатов
# 1) проверка открытия корзины.
def cart():
    proverka = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class*=breadcrumb-heading]"))).text
    proverka1 = "Корзина"
    assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"
    print("Корзина открыта")

# 2)проверка товара в корзине.
# def quantity_cart():
#     proverka = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class*=breadcrumb-heading]"))).text
#     proverka1 = "Корзина"
#     assert proverka == proverka1, f"Тест не пройден и вот результат - {proverka}"

cart()

# cart(), quantity_cart()