from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # open link in browser
    x = browser.find_element_by_id("treasure").get_attribute("valuex")
# вытягиваем со страницы значение х

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
# рассчмиываем функцию
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
# input answer in field
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
# click on checkbox
    option1 = browser.find_element_by_id("robotsRule")
    option1.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
