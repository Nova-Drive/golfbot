from time import sleep
from datetime import datetime, time, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

OPEN_TIME = '07:00:00.500000'
ANTI_TIMEOUT = '06:58:00'

username = ""
password = ""

with open("login.txt", "r") as file:
    username = file.readline().strip()
    password = file.readline().strip()
    file.close()



options = webdriver.FirefoxOptions()
# new tab instead of new window
options.add_argument("--new-tab")
driver = webdriver.Firefox(options=options)
driver.maximize_window()

driver.implicitly_wait(60)

driver.get("https://www.tee-on.com/PubGolf/servlet/com.teeon.teesheet.servlets.golfersection.ComboLanding?CourseCode=RDTL&FromCourseWebsite=true")

startTime = datetime.strptime(ANTI_TIMEOUT, '%H:%M:%S').time()
while datetime.now().time() < startTime:
    pass

# Hit the member button
member_button = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/a[2]')
member_button.click()

# Enter the username

username_field = driver.find_element(By.ID, 'Username')
username_field.send_keys(username)
password_field = driver.find_element(By.ID, 'Password')
password_field.send_keys(password)

login_button = driver.find_element(By.ID, 'sign-in-btn')
login_button.click()

# Select the proper date
sleep(1)
date_button = driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div[2]/div/div/div/div/div/div/div[1]/form/div[1]/select/option[9]')
date_button.click()

# Select the proper time
time_button = driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div[2]/div/div/div/div/div/div/div[1]/form/div[2]/select/option[14]')
time_button.click()

# Select the proper number of holes
holes_button = driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div[2]/div/div/div/div/div/div/div[1]/form/div[3]/div/div/label[1]')
holes_button.click()

# Select the proper number of players
players_button = driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div[2]/div/div/div/div/div/div/div[1]/form/div[4]/div/div/label[1]')
players_button.click()

# Deselect RedTail
redtail_button = driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div[2]/div/div/div/div/div/div/div[1]/form/div[5]/div/div[1]/div/div/table/tbody/tr[4]/td[1]/label')
redtail_button.click()

# Select search button

scrollable_element = driver.find_element(By.XPATH, '//*[@id="scrollbar-wrapper"]')
driver.execute_script("arguments[0].scroll(0, arguments[0].scrollHeight);", scrollable_element)
search_button = driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div[2]/div/div/div/div/div/div/div[1]/form/a[2]')
sleep(0.5)
ActionChains(driver).scroll_to_element(search_button).perform()

startTime = datetime.strptime(OPEN_TIME, '%H:%M:%S.%f').time()
print(startTime)
while datetime.now().time() < startTime:
    pass

search_button.click()

#sleep(1)

# Select the proper time
time_button = driver.find_element(By.XPATH, '/html/body/div[8]/div[2]/div[2]/div/div/div/div/div/form/div[5]/div[1]/div[1]/a')
time_button.click()

sleep(2)
driver.refresh()
