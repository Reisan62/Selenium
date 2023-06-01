from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('C:\\Users\\baldy\\PycharmProjects\\python_selenium\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

print("Добро пожаловать в наш магазин!")
print("Выберите один из следующих товаров и укажите его номер: 1 - Sauce Labs Backpack, 2 - Sauce Labs Bike Light, 3 - Sauce Labs Bolt T-Shirt, 4 - Sauce Labs Fleece Jacket, 5 - Sauce Labs Onesie, 6 - Test.allTheThings() T-Shirt (Red)")


class Product():
    """Создаем продукт"""

    def __init__(self, name, id, price ,add_cart, cart_id, cart_price, finish_id, finish_price ):
        """Инициализируем атрибуты продукта"""
        self.name = name
        self.id = id
        self.price = price
        self.add_cart = add_cart
        self.cart_id = cart_id
        self.cart_price = cart_price
        self.finish_id = finish_id
        self.finish_price = finish_price

    def test (self):
        """Совершаем тест продукта"""
        print("    Step 1")
        user_name = driver.find_element(By.ID, "user-name")
        user_name.send_keys("standard_user")
        print("Input Login")
        password = driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")
        print("Input password")
        button_login = driver.find_element(By.ID, "login-button").click()
        print("click login button")

        """INFO Product #1"""
        print("    Step 2")
        product_1 = driver.find_element(By.XPATH, self.id)
        value_product_1 = product_1.text
        print(value_product_1)

        price_product_1 = driver.find_element(By.XPATH, self.price)
        value_price_product_1 = price_product_1.text
        print(value_price_product_1)

        select_product_1 = driver.find_element(By.XPATH, self.add_cart).click()
        print("Select Product 1")

        cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        print("Enter Cart")

        """Info Cart Product 1"""
        print("    Step 3")
        cart_product_1 = driver.find_element(By.XPATH, self.cart_id)
        value_cart_product_1 = cart_product_1.text
        print(value_cart_product_1)
        assert value_product_1 == value_cart_product_1
        print("INFO Cart Product 1 GOOD")

        price_cart_product_1 = driver.find_element(By.XPATH, self.cart_price)
        value_price_cart_product_1 = price_cart_product_1.text
        print(value_price_cart_product_1)
        assert value_price_product_1 == value_price_cart_product_1
        print("INFO Cart Price Product 1 GOOD")

        checkout = driver.find_element(By.ID, "checkout").click()
        print("Click checkout")

        """Select User Info"""
        print("    Step 4")
        first_name = driver.find_element(By.ID, "first-name" )
        first_name.send_keys("Alex")
        print("Input First name")
        last_name = driver.find_element(By.ID, "last-name")
        last_name.send_keys("ivanov")
        print("Input Last name")
        zip_code = driver.find_element(By.ID, "postal-code")
        zip_code.send_keys("361432")
        print("Input Zip code")
        continue_botton = driver.find_element(By.ID, "continue").click()
        print("Click Continue")

        """INFO Finish Product 1"""
        print("    Step 5")
        finish_product_1 = driver.find_element(By.XPATH, self.finish_id)
        value_finish_product_1 = finish_product_1.text
        print(value_finish_product_1)
        assert value_product_1 == value_finish_product_1
        print("INFO Finish Product 1 GOOD")

        price_finish_product_1 = driver.find_element(By.XPATH, self.finish_price)
        value_price_finish_product_1 = price_finish_product_1.text
        print(value_price_finish_product_1)
        assert value_price_product_1 == value_price_finish_product_1
        print("INFO Finish Price Product 1 GOOD")

        summary_price = driver.find_element(By.CLASS_NAME, "summary_subtotal_label")
        value_summary_price = summary_price.text
        print(value_summary_price)
        item_total = "Item total: " + value_price_finish_product_1
        print(item_total)
        assert value_summary_price == item_total
        print("Total summary price GOOD0")

        """Finish"""
        print("    Step 6")
        finish_button = driver.find_element(By.ID, "finish").click()
        print("Click Finish Button")
        thank = driver.find_element(By.CLASS_NAME, "complete-header").text
        assert thank == "Thank you for your order!"
        print("All test DONE")

sauce_labs_backpack = Product(1, "//*[@id='item_4_title_link']","/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div", "//*[@id='add-to-cart-sauce-labs-backpack']", "//*[@id='item_4_title_link']", "//div[@class='inventory_item_price']","//*[@id='item_4_title_link']", "//div[@class='inventory_item_price']")
sauce_labs_bike_light = Product(2, "//*[@id='item_0_title_link']", "/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div", "//*[@id='add-to-cart-sauce-labs-bike-light']", "//*[@id='item_0_title_link']", "//div[@class='inventory_item_price']", "//*[@id='item_0_title_link']", "//div[@class='inventory_item_price']")
sauce_labs_bolt_t_shirt = Product(3, "//*[@id='item_1_title_link']", "/html/body/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div", "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']", "//*[@id='item_1_title_link']", "//div[@class='inventory_item_price']", "//*[@id='item_1_title_link']", "//div[@class='inventory_item_price']")
sauce_labs_fleece_jacket = Product(4, "//*[@id='item_5_title_link']", "/html/body/div/div/div/div[2]/div/div/div/div[4]/div[2]/div[2]/div", "//*[@id='add-to-cart-sauce-labs-fleece-jacket']", "//*[@id='item_5_title_link']", "//div[@class='inventory_item_price']", "//*[@id='item_5_title_link']", "//div[@class='inventory_item_price']")
sauce_labs_onesie = Product(5, "//*[@id='item_2_title_link']", "/html/body/div/div/div/div[2]/div/div/div/div[5]/div[2]/div[2]/div", "//*[@id='add-to-cart-sauce-labs-onesie']", "//*[@id='item_2_title_link']", "//div[@class='inventory_item_price']", "//*[@id='item_2_title_link']", "//div[@class='inventory_item_price']")
test_allTheThings_t_Shirt = Product(6, "//*[@id='item_3_title_link']", "/html/body/div/div/div/div[2]/div/div/div/div[6]/div[2]/div[2]/div", "//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']", "//*[@id='item_3_title_link']", "//div[@class='inventory_item_price']", "//*[@id='item_3_title_link']", "//div[@class='inventory_item_price']")
def vhod():
    product = input()
    if product == "1":
        print("Вы выбрали: Sauce Labs Backpack")
        sauce_labs_backpack.test()
    elif product == "2":
        print("Вы выбрали: Sauce Labs Bike Light")
        sauce_labs_bike_light.test()
    elif product == "3":
        print("Вы выбрали: Sauce Labs Bolt T-Shirt")
        sauce_labs_bolt_t_shirt.test()
    elif product == "4":
        print("Вы выбрали: Sauce Labs Fleece Jacket")
        sauce_labs_fleece_jacket.test()
    elif product == "5":
        print("Вы выбрали: Sauce Labs Onesie")
        sauce_labs_onesie.test()
    elif product == "6":
        print("Вы выбрали: Test.allTheThings() T-Shirt (Red)")
        test_allTheThings_t_Shirt.test()
    else:
        print("Вы ввели не тот символ, пожалуйста, введите цифру от 1 до 6")
        vhod()
vhod()