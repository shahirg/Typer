from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from time import sleep
import keyboard

from keys import type_test
from model import text_from_img


driver = webdriver.Chrome("C:\Webdrive\chromedriver");
def find(xpath):
    driver.find_element_by_xpath(xpath)
def find_click(xpath):
    driver.find_element_by_xpath(xpath).click()
def find_send_key(xpath,key):
    driver.find_element_by_xpath(xpath).send_keys(key)

def load():
    driver.get("https://monkeytype.com")
    driver.maximize_window()
    setting = "//i[@class = 'fas fa-fw fa-cog']"
    reset = "//h1[text() ='quick tab mode']/..//div[@class = 'button on']"
    caret = "//h1[text() ='caret style']/..//div[@caretstyle = 'off']"

    typo = "//h1[text() ='indicate typos']/..//div[@class = 'button on']"
    sleep(1)
    find_click(setting)
    sleep(1)
    find_click(caret)
    sleep(1)
    find_click(typo)
    sleep(1)
    find_click(reset)

    
def new_test():
    keyboard.press('tab')
    sleep(1)

def capture():
    driver.save_screenshot("screenshots\screen.png")
if __name__ == "__main__":
    load()
    new_test()
    capture()
    pixels = [400,520,480,1500]
    type_test(text_from_img("screenshots\screen.png",crop_pixs=pixels))
    pixels = [440,520,480,1500]
    while(True):
        capture()
        type_test(text_from_img("screenshots\screen.png",crop_pixs=pixels))
