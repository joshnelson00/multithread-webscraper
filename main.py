from selenium import webdriver
from selenium.webdriver.common.by import By
# Config options for the ChromeDriver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# Get URL from the User
while True:
    url = str(input("Please Enter URL:"))
    if isinstance(url, str):
        break
    print("Invalid URL: Please Try Again")

driver.get(url)
print(driver.page_source)


driver.close()