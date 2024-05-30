from time import sleep
from datetime import datetime, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

OPEN_TIME = '07:00'
ANTI_TIMEOUT = '06:58'

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# options.add_argument("--start-maximized")
# driver = webdriver.Chrome(options=options)

options = webdriver.FirefoxOptions()
# new tab instead of new window
options.add_argument("--new-tab")
driver = webdriver.Firefox(options=options)
driver.maximize_window()

driver.implicitly_wait(5)

driver.get("https://www.tee-on.com/PubGolf/servlet/com.teeon.teesheet.servlets.golfersection.ComboLanding?CourseCode=RDTL&FromCourseWebsite=true")

startTime = time(*(map(int, ANTI_TIMEOUT.split(':'))))
while datetime.now().time() < startTime:
    pass

# Hit the member button
member_button = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/a[2]')
member_button.click()

# Enter the username

username_field = driver.find_element(By.ID, 'Username')
username_field.send_keys('')
password_field = driver.find_element(By.ID, 'Password')
password_field.send_keys('')

login_button = driver.find_element(By.ID, 'sign-in-btn')
login_button.click()

# Select the proper date
sleep(1)
date_button = driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div[2]/div/div/div/div/div/div/div[1]/form/div[1]/select/option[9]')
date_button.click()

# Select the proper time
time_button = driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div[2]/div/div/div/div/div/div/div[1]/form/div[2]/select/option[15]')
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

# try:
#     ActionChains(driver).scroll_to_element(search_button).perform()
# except:
#     ActionChains(driver).scroll_to_element(search_button).perform()
#     pass


startTime = time(*(map(int, OPEN_TIME.split(':'))))
while datetime.now().time() < startTime:
    pass

search_button.click()

sleep(1)

# Select the proper time
time_button = driver.find_element(By.XPATH, '/html/body/div[8]/div[2]/div[2]/div/div/div/div/div/form/div[5]/div[1]/div[1]/a')
time_button.click()

sleep(3)
driver.refresh()
