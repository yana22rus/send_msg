from os import devnull
from time import sleep
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import pickle


options = Options()
options.headless = False
driver = webdriver.Firefox(options=options,service_log_path=devnull)

driver.maximize_window()
driver.implicitly_wait(3)

driver.get('https://m.vk.com/')


for cookie in pickle.load(open("cookies","rb")):

    driver.add_cookie(cookie)

sleep(5)

driver.refresh()

for x in range(1,11):

    try:

        driver.get('ссылка')

        driver.find_element_by_xpath('//a/div[2]/div[2]/div').click()

        driver.find_element_by_css_selector('#attach_photo_btn > .i_icon').click()

        sleep(2)

        driver.find_element_by_link_text('Файл').click()

        sleep(1)

        driver.find_element_by_css_selector('.iwrap:nth-child(1) > .textfield').send_keys(f'gif{x}.gif')

        driver.find_element_by_css_selector('.al_tab').click()

        driver.find_element_by_css_selector('a > .si_owner').click()

        driver.find_element_by_css_selector('#write_submit').click()

    except Exception:

        continue