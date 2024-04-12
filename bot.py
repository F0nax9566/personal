import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

u = "username"
p = "password"
s = "target username"
spam_message = "message"
PATH = r"C:\Users\F0nax\Desktop\code\chromedriver\chromedriver.exe"

options = Options()
options.add_argument('--start-maximized')

service = Service(PATH)
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.instagram.com")

wait = WebDriverWait(driver, 20)

userName = wait.until(EC.presence_of_element_located((By.NAME, "username")))
password = driver.find_element(By.NAME, "password")
userName.send_keys(u)
password.send_keys(p)
password.send_keys(Keys.RETURN)

try {
    save_info_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "yWX7d")))
    save_info_button.click()
} except:
    pass

driver.get("https://www.instagram.com/direct/inbox/")
time.sleep(2)

try {
    skip_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "HoLwm")))
    skip_button.click()
} except:
    pass

new_message_button = wait.until(EC.presence_of_element_located(
    (By.XPATH, "//*[@id='react-root']/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button")))
new_message_button.click()

search_box = wait.until(EC.presence_of_element_located((By.NAME, "queryBox")))
search_box.send_keys(s)
search_box.send_keys(Keys.RETURN)

user_div = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div[2]/div[2]/div[1]")))
user_div.click()

next_button = wait.until(EC.presence_of_element_located(
    (By.XPATH, "/html/body/div[5]/div/div/div[1]/div/div[2]/div/button/div")))
next_button.click()

message_text = wait.until(EC.presence_of_element_located(
    (By.XPATH, "//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")))
message_text.send_keys(spam_message)
message_text.send_keys(Keys.RETURN)
time.sleep(2)

for _ in range(200):
    message_text.send_keys(spam_message)
    message_text.send_keys(Keys.RETURN)
    time.sleep(2)
