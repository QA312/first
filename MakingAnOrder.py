# Импорт библиотеки вебдрайвера
from selenium import webdriver
# Импортируем иблиотеку времени time, для ожидания прогрузки страницы
import time
# Импорт библиотеки By
from selenium.webdriver.common.by import By
# Импорт библиотеки Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Импорт библиотеки Faker
from faker import Faker

#-----------------инициализация библиотеки для firefox-------------
from selenium.webdriver.firefox.options import Options
#-----------------инициализация библиотеки для firefox-------------
#-----------------Использование Jenkins в headless режиме (без графического интерфейса)----------------
options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)
#-----------------Использование Jenkins в headless режиме (без графического интерфейса)----------------
fake = Faker(locale="ru_RU")
link = "http://qa228.karpin74.beget.tech/"
# browser = webdriver.Firefox() #----отключили для запуска теста для jenkins вне графического интерфейса-----
browser.maximize_window()
browser.get(link)

#----------------Подготовка рандомизации данных полей-------------------------
randomName = fake.name()
a = randomName.split()
name = a[0]
last_name = a[1]

randomAddress = fake.address()
b = randomAddress.split()
address = b[2:6]
punkt = b[1:5]
oblast = b[0:2]
index = b[-1]

phone = fake.phone_number()

randomEmail = fake.email()

#--------------------------Тело основного кода--------------------------------------
#----------Переход в меню "Магазин"----------------------------------------------
mag = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[2]/nav/div[1]/ul/li[1]/a").click()
#----------Выбор категории "Все товары"------------------------------------------
# mag2 = browser.find_element(By.CSS_SELECTOR, "#st-primary-content > div.woocommerce.columns-4 > ul > li:nth-child(2) > a > h2").click()
#------Использовали наиболее устойчивиый метод-----------------
mag2 = browser.find_element(By.CSS_SELECTOR, "h2[class*=woocommerce-loop-category__title]").click()
#------Клик по кнопке "Будуильники"--------------------------------------------
mag3 = browser.find_element(By.CSS_SELECTOR, "div[class*=product-img]").click()
#------Очистка значения количества товара-----------------------------------
quantity = browser.find_element(By.CSS_SELECTOR, "input[type*=number]").clear()
#------Указали количество товара равное 5------------------------------------
quantity = browser.find_element(By.CSS_SELECTOR, "input[type*=number]").send_keys("5")
#----------------------------Работа с корзиной/cart--------------------------
#------Клик по кнопке "В корзину"--------------------------------------------
product = browser.find_element(By.CSS_SELECTOR, "button[name*=add-to-cart]").click()
#------Клик по иконке "Корзина"/Cart, всплытие модального окна Корзины--------
product = browser.find_element(By.CSS_SELECTOR, "i[class*=fa-shopping-cart]").click()
#------Используем ожидание отрисовки модального окна корзины------------------
cartmodal = WebDriverWait(browser, 5).until(
EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class*=cart-container]")))
#time.sleep(2)
#------Клик по иконке "Просмотреть корзину"--------
product = browser.find_element(By.CSS_SELECTOR, "a[class*=cart-ft-btn]").click()
#------Клик по кнопке "Оформить заказ"-------------
checkout = browser.find_element(By.CSS_SELECTOR,"#st-primary-content > div > div.cart-collaterals > div > div > a").click()

#------------------------Страница Оформления заказа-----------------------------------
fieldName = browser.find_element(By.CSS_SELECTOR, "#billing_first_name")
fieldName.send_keys(name)

fieldName = browser.find_element(By.CSS_SELECTOR, "#billing_last_name")
fieldName.send_keys(last_name)

fieldHome = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/section/div/div/div/div/form[2]/div[1]/div[1]/div/div/p[5]/span/input")
fieldHome.send_keys(address)

fieldHome = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/section/div/div/div/div/form[2]/div[1]/div[1]/div/div/p[7]/span/input")
fieldHome.send_keys(punkt)

fieldHome = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/section/div/div/div/div/form[2]/div[1]/div[1]/div/div/p[8]/span/input")
fieldHome.send_keys(oblast)

fieldHome = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/section/div/div/div/div/form[2]/div[1]/div[1]/div/div/p[9]/span/input")
fieldHome.send_keys(index)

fieldHome = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/section/div/div/div/div/form[2]/div[1]/div[1]/div/div/p[10]/span/input")
fieldHome.send_keys(phone)

fieldHome = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/section/div/div/div/div/form[2]/div[1]/div[1]/div/div/p[11]/span/input")
fieldHome.send_keys(randomEmail)

#checkbox = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/section/div/div/div/div/form[2]/div[2]/div/div/label/input").click()
#search_string = browser.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div[1]/div/div/div/div/div[2]/div/form/input[2]")
#search_string.send_keys(" ")
# making_an_order = browser.find_element(By.NAME, "button[woocommerce_checkout_place_order]").click()
time.sleep(2)
# making_an_order = browser.find_element(By.NAME, "woocommerce_checkout_place_order").click()
making_an_order = browser.find_element(By.NAME, "woocommerce_checkout_place_order")
making_an_order.click()