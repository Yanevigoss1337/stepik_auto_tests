from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(2)

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button1 = browser.find_element_by_css_selector("button.btn")
    button1.click()

finally:
    time.sleep(10)

    browser.quit()

