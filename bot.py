from config import keys
from selenium import webdriver
import time

def order(k):
    driver.get(k['product_url'])

    driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
    time.sleep(.5)
    driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()

    # personal info
    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(k["name"])
    driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(k["email"])
    driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(k["phone"])
    driver.find_element_by_xpath('//*[@id="bo"]').send_keys(k["address"])
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(k["zip"])
    driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(k["city"])

    # payment
    driver.find_element_by_xpath('//*[@id="rnsnckrn"]').send_keys(k["card"])
    driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(k["cvv"])
    driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[4]').click()
    driver.find_element_by_xpath('//*[@id="credit_card_year"]/option[3]').click()

    # ADD MORE FUNCTIONALITY BY ADDING MONTH TO CONFIG FILE
    # driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[{month}]').format(k["card_month"]).click
    # YEAR NEEDS TO BE CHANGED EVERY YEAR BY 1-10 1 BEING CURRENT YEAR

    # terms and conditions & process payment
    driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p/label/div/ins').click()
    driver.find_element_by_xpath('//*[@id="pay"]/input').click()

if __name__ == '__main__':
    driver = webdriver.Chrome('./chromedriver')
    order(keys)