import os
from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("[placeholder='Enter first name']")
    input1.send_keys("Igor")

    input2 = browser.find_element_by_css_selector("[placeholder='Enter last name']")
    input2.send_keys("Petrov")

    input3 = browser.find_element_by_css_selector("[placeholder='Enter email']")
    input3.send_keys("mail@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '123.txt')  # добавляем к этому пути имя файла

    element = browser.find_element_by_id("file")  # ищем кнопку прикладывания файла
    element.send_keys(file_path)  # прикладываем файл по известному пути

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()