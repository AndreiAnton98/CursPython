from selenium import webdriver
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
#driver.maximize.window()
driver.get('https://www.cel.ro/index.php?main_page=login')