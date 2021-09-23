from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    y_element = browser.find_element_by_id("num2")
    x = int(x_element.text)
    y = int(y_element.text)
    z = str(str(int(x)+int(y)))

    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector("[value='z']").click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()