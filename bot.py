from selenium import webdriver
from config import keys
import time

def supreme_order(k):
    driver.get(k['supreme_url'])

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


def nike_order(k):
    driver.get(k['nike_url'])
    driver.find_element_by_xpath("//button[text()='Join / Log In']").click()
    driver.find_element_by_xpath("//input[@type='email']").send_keys(k["nike_email"])
    driver.find_element_by_xpath("//input[@type='password']").send_keys(k["nike_password"])
    driver.find_element_by_xpath("//input[@value='SIGN IN']").click()

    #driver.find_element_by_xpath("//li[@data-qa='size-available']").find_element_by_xpath("//button[text()='{}']".format(k["shoe_size"])).click()


def adidas_order(k):
    driver.get(k['adidas_url'])
    #login adidas
    #new tab with shoes
    #buy shoes
    
if __name__ == '__main__':
    driver = webdriver.Chrome('./chromedriver')
    #driver = webdriver.Firefox(executable_path = './geckodriver')
    nike_order(keys)
