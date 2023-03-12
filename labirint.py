from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#Для явного ожидания
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#from time import sleep

SelectList = '#catalog-navigation > form > div.desktop-subnavigagions-block.only_desc > div:nth-child(1) > div > div > span.navisort-part.navisort-view.navisort-part-6.fright > span > a.radioitems-item.view-table'
book1 = '#buy464095'
url = 'https://labirint.ru/'
SearchWord = 'Java'
cookie = {
    'name': 'cookie_policy',
    'value' : '1'
}
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
locator = 'table.products-table'

#Oткрываем сайт
def openLabirint():
   browser.get(url)
   browser.add_cookie(cookie)
   browser.implicitly_wait(4)
   browser.maximize_window()

#Вводим Java в поиск и кликаем по кнопке найти
def Search(word):
   browser.find_element(By.CSS_SELECTOR,'#search-field').send_keys(word)
   browser.find_element(By.CSS_SELECTOR,'button[type=submit]').click()

#Выбираем вид "список"
def SwitchToTable():
   browser.find_element(By.CSS_SELECTOR,SelectList).click()
   #Добавим неявное ожидание, чтобы успело подгрузить список
   #sleep(5)
   #ИЛИ Добавим явное ожидание
   WebDriverWait(browser, 9).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))

#Добавляем в корзину выбранные книги
def AllBuy():
   buttons = browser.find_elements(By.CSS_SELECTOR,'a.buy-link')
   counter = 0
   for i in range(0, len(buttons)):
      buttons[i].click()
      counter = counter + 1
   print('Нажали ' + str(counter) + ' раз') 
   return counter

#Открываем корзину
def OpenCart():
   browser.get(url + '/cart/')

#Проверяем условие задачи   
def CheckTabContains(text):
   ElementText = browser.find_element(By.CSS_SELECTOR, '#ui-id-4').text
   if str(text) in ElementText:
      print('Есть 60 книг')
   else:
      print('Нет 60 книг')  
      openLabirint()


openLabirint()
Search(SearchWord)
SwitchToTable()
count = AllBuy()
OpenCart()
CheckTabContains(count)
browser.quit