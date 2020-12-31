from config import keys
from selenium import webdriver
import time

def order(k):
    driver.get(k['product_url'])

    driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
    time.sleep(.1)
    driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()

    # personal info
    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(k["name"])
    driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(k["email"])
    driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(k["phone"])
    driver.find_element_by_xpath('//*[@id="bo"]').send_keys(k["address"])
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(k["zip"])
    driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(k["city"])

    # card info/payment
    driver.find_element_by_xpath('//*[@id="rnsnckrn"]').send_keys(k["card"])
    driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(k["cvv"])
    driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[{}]'.format(k["card_month"])).click()
    driver.find_element_by_xpath('//*[@id="credit_card_year"]/option[{}]'.format(k["card_year"])).click()

    # terms and conditions & process payment
    driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p/label/div/ins').click()
    driver.find_element_by_xpath('//*[@id="pay"]/input').click()

if __name__ == '__main__':
    #driver = webdriver.Chrome('./chromedriver')
    driver = webdriver.Firefox(executable_path = './geckodriver')
#if user selects chrome or firefox set driver = 
    order(keys)