from selenium import webdriver
import time

#x8ueH8KrhKpglo


#заполнение 5 обязательных полей валидными значениями


link = "https://area.mtg-bi.com/sign"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element_by_id("signup-name")
    name.send_keys("Ivan")
    email = browser.find_element_by_id("signup-email")
    email.send_keys("ghjkll@mail.ru")
    password = browser.find_element_by_id("signup-pass")
    password.send_keys("123654")
    confirm = browser.find_element_by_id("signup-confirm")
    confirm.send_keys("123654")
    code = browser.find_element_by_id("invitation-code")
    code.send_keys("x8ueH8KrhKpglo")

    button = browser.find_element_by_css_selector("button.footer__btn")
    button.click()

finally:
    # успеваем просмотреть за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла






