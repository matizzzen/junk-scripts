from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

users = [['Русак Александр', '\\00.Scans\\rusak.a'], ['Селезнева Евгения', '\\00.Scans\\selezneva.e'], ['Перель Иван', '\\00.Scans\\perel.i'], ['Руткевич Юлия', '\\00.Scans\\rutkevich.u'], ['Суворова Светлана', '\\00.Scans\\suvorova.s'], ['Шабалтас Артем', '\\00.Scans\\shabaltas.a'], ['Швецов Игорь', '\\00.Scans\\shvetsov.i'], ['Щетинщиков Вячеслав', '\\00.Scans\\schetinshikov.v'], ['Нежников Андрей', '\\00.Scans\\nezhnikov.a'], ['Хмеленко Евгений', '\\00.Scans\\khmelenko.e'], ['Ушканс Андис', '\\00.Scans\\ushkans.a'], ['Шкамбарный Илья', '\\00.Scans\\shkambarniy.i'], ['Сидорова Татьяна', '\\00.Scans\\sidorova.t'], ['Мишустина Надежда', '\\00.Scans\\mishustina.n'], ['Дежурная Марина', '\\00.Scans\\Dezhurnaia.m'], ['Земляков Олег', '\\00.Scans\\zemlyakov.o'], ['Черных Алексей', '\\00.Scans\\chernyh.a'], ['Симоненкова Елена', '\\00.Scans\\simonenkova.e'], ['Борисов Дмитрий', '\\00.Scans\\borisov.d'], ['Пойменова Полина', '\\00.Scans\\poimenova.p'], ['Шамиль Багомедов', '\\00.Scans\\bagomedov.s'], ['Кондакова Юлия', '\\00.Scans\\kondakova.u'], ['Хватов Александр', '\\00.Scans\\hvatov.a'], ['Виноградова Светлана', '\\00.Scans\\vinogradova.s'], ['Панкратов Владимир', '\\00.Scans\\pankratov.v'], ['Байметов Михаил', '\\00.Scans\\baimetov.m'], ['Апридонидзе Роман', '\\00.Scans\\apridonidze.r'], ['Барановская Наталья', '\\00.Scans\\baranovskaya.n'], ['Ульянова Любовь', '\\00.Scans\\ulyanova.l'], ['Головлева Оксана', '\\00.Scans\\golovleva.o'], ['Денисова Маргарита', '\\00.Scans\\denisova.m'], ['Иванов Олег', '\\00.Scans\\ivanov.o'], ['Ильинский Андрей', '\\00.Scans\\ilinskiy.a'], ['Кузьмина Светлана', '\\00.Scans\\kuzmina.s'], ['Ляшкин Николай', '\\00.Scans\\lyashkin.n'], ['Нежникова Екатерина', '\\00.Scans\\nezhnikova.e'], ['Никишин Алексей', '\\00.Scans\\nikishin.a'], ['Калинина Елена', '\\00.Scans\\kalinina.e'], ['Кучерова Софья', '\\00.Scans\\kucherova.s'], ['Бергамен Татьяна', '\\00.Scans\\bergamen.t'], ['Мартынова Ольга', '\\00.Scans\\martynova.o']]

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('http://10.0.0.94:8000/rps/albody.cgi')

driver.maximize_window()

driver.find_element(By.NAME, 'USERNAME').send_keys('Administrator')
driver.find_element(By.NAME, 'PASSWORD_T').send_keys('2468')

driver.find_element(By.NAME, 'LoginButtonP').click()
driver.find_element(By.CLASS_NAME, 'ButtonEnable').click()

driver.find_element(By.XPATH, r'//*[@id="navGeneral"]/ul/li[3]/a').click()
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.find_element(By.XPATH, r'//*[@id="subAddressBookList"]/div/div[2]/table/tbody/tr[1]/td[1]/a[1]').click()  # book

for user in users:
    driver.find_element(By.XPATH, r'//*[@id="contents"]/div[4]/div/div[1]/fieldset[1]/input[1]').click()  # new user
    sel = Select(driver.find_element(By.XPATH, r'//*[@id="Class"]'))
    sel.select_by_visible_text('File')
    driver.find_element(By.XPATH, r'//*[@id="Class_Button"]').click()
    driver.find_element(By.XPATH, r'//*[@id="ANAME"]').send_keys(user[0])  # name
    driver.find_element(By.XPATH, r'//*[@id="AAD1"]').send_keys(r'\\Antey-NAS\CORP')  # host
    driver.find_element(By.XPATH, r'//*[@id="FldPathBtn"]').click()  # settings
    driver.find_element(By.XPATH, r'//*[@id="APATH"]').send_keys(user[1])  # path
    driver.find_element(By.XPATH, r'//*[@id="AUSER"]').send_keys(r'scanner')  # use scanner
    driver.find_element(By.XPATH, r'//*[@id="APWORD"]').send_keys('Skanner_23Skanner_23')  # pwd1
    driver.find_element(By.XPATH, r'//*[@id="APWORD_RE"]').send_keys('Skanner_23Skanner_23')  # pwd2
    # driver.find_element(By.XPATH, r'//*[@id="INPUT_PSWD"]').click() # check
    driver.find_element(By.XPATH, r'//*[@id="contents"]/div[3]/fieldset/input[1]').click()  # ok1
    driver.find_element(By.XPATH, r'//*[@id="OK_Button"]').click()  # ok2
while True:
    pass
