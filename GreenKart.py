from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pytestdemo.conftest import browserinstance


def test_greenkart(browserinstance):
    chrome_optns = webdriver.ChromeOptions
    chrome_optns.add_argument("headless")

expectedList=['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
actualList=[]
driver = browserinstance
driver = webdriver.Chrome(options=chrome_optns)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
productList = driver.find_elements(By.CSS_SELECTOR,"div [class=product]")

count = 0
print("Product Price")
for product in productList:
    actualList.append(product.find_element(By.CSS_SELECTOR,"div h4").text)
    price = product.find_element(By.CSS_SELECTOR, "div p")
    print(f"{count}:{price.text}")
    count=count+1
    product.find_element(By.XPATH,".//div/button").click()

print()
print("Product counts")
ProductCounts = len(productList)
print(ProductCounts)
print()

print("Actual product List")
print(actualList)
print()

print("Expected product List")
print(expectedList)

driver.find_element(By.CSS_SELECTOR,".cart-icon").click()
driver.find_element(By.XPATH,"//button[contains(text(), 'PROCEED TO CHECKOUT')]").click()
cartDetails = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(2) p")
quanities = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(3) p")
Prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(4) p")
Totals= driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")

print("Products in cart")
for cartDetail in cartDetails:
    print(f"Product_name:- {cartDetail.text}")
print()
print("Products qty in cart")
for  qty in quanities:
    print(f"Product qty:- :{qty.text}")
print()
print("Products price in cart")
for PPrice in Prices:
    print(f"Product price is:- {PPrice.text}")
print()
print("Product total price in cart")
for Total in Totals:
    print(f"Product total price:- {Total.text}")
print()

print("Total MRP is:- ")
amount1 = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(4) p")
sum1 = 0
for mrp in amount1:
    sum1 = sum1 + float(mrp.text)
print(sum1)
print()

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".promoInfo")))
promoInfo = driver.find_element(By.CSS_SELECTOR,".promoInfo").text
print("Promo code status")
print(promoInfo)

print("Total price")
amounts= driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum=0
for amount in amounts:
    sum = sum + float(amount.text)
print(sum)
print()

print("Discounted Price")
After_Discount = driver.find_element(By.CSS_SELECTOR,"span[class='discountAmt']").text
After_Discount = float(After_Discount)
print(After_Discount)

assert After_Discount < sum

assert actualList == expectedList, f"Mismatch! Actual: {actualList}, Expected: {expectedList}"

#place order
driver.find_element(By.XPATH,"//button[normalize-space()='Place Order']").click()
Countries =  driver.find_element(By.CSS_SELECTOR,"select:nth-child(1)").text
cntry =0
for CountryName in Countries:
    print(f"{cntry}:{CountryName.title()}")
    cntry=cntry+1
driver.quit()