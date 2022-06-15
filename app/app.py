from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pathlib import Path
import time
URL = "https://www.mos.ru/otvet-transport/kak-proverit-razreshenie-taksi/"
BASE_DIR = Path(__file__).resolve().parent
chrome_driver_path = BASE_DIR.joinpath('chromedriver.exe')
my_data_example = {
    'code':'123город',
    'driver_name':'Василий Пупкин',
    'car_num':'a048xx799'
}
def main():
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get(URL)
    time.sleep(5)
    inputCode = driver.find_element(by=By.XPATH, value="//input[contains(@name, 'regnum')]")
    inputCode.send_keys(my_data_example.get('code'))
    inputDriver = driver.find_element(by=By.XPATH, value="//input[contains(@name, 'fullname')]")
    inputDriver.send_keys(my_data_example.get('driver_name'))
    inputCarNum = driver.find_element(by=By.XPATH, value="//input[contains(@name, 'licensenum')]")
    inputCarNum.send_keys(my_data_example.get('car_num'))
    time.sleep(10)


if __name__=="__main__":
    main()