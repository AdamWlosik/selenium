from selenium.webdriver import ChromeOptions, Chrome

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(options=opts)
driver.get("https://google.com")

