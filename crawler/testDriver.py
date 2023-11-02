from selenium import webdriver

service = webdriver.ChromeService(executable_path="./chromedriver/chromedriver")
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")

# options.binary_location = CHROME_LOCATION
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://selenium.dev")

driver.quit()

