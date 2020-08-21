from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

#Обновление личной информации пользователя, которое доступно после авторизации (profile)


link = "https://area.mtg-bi.com/sign"
try:
    browser = webdriver.Chrome()
    browser.get(link)


    entrance = browser.find_element_by_css_selector("ul.navbar-nav")
    entrance.click()
    browser.implicitly_wait(15)
    login = browser.find_element_by_id("signin-login")
    login.send_keys("testcaseqa5@gmail.com")
    password = browser.find_element_by_id("signin-pass")
    password.send_keys("123456")
    button = browser.find_element_by_css_selector("button.sign__submit")
    button.click()

    time.sleep(5)

    #обновляем информацию о пользователе

    user1 = browser.find_element_by_css_selector(".navbar-toggler")
    user1.click()

    user2 = browser.find_element_by_css_selector(".fa-user-circle.mx-3")
    user2.click()

    user3 = browser.find_element_by_css_selector(".fa-user.mr-3")
    user3.click()

    country = Select(browser.find_element_by_id("profile-country"))
    country.select_by_value("RU")
    phone = browser.find_element_by_id("profile-phone")
    phone.send_keys("9201856325")
    busseg = Select(browser.find_element_by_id("profile-busseg"))
    busseg.select_by_value("12")

    button = browser.find_element_by_css_selector("button.sign__submit")
    button.click()

    # находим элемент c текстои "Успех"
    success_text = browser.find_element_by_css_selector(".fade.show strong")
    # записываем в переменную success текст из элемента success_text
    success = success_text.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Success!" == success

finally:
    # успеваем просмотреть за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла






