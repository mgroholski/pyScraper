#BROKEN

from bs4 import BeautifulSoup
import sqlite3
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

#Enter username and password
#REMOVE USERNAME AND PASSWORD
uname = str(input("Username: "))
password = str(input("Password: "))


username = str(input("Username of Trackee: "))
conn = sqlite3.connect("follower.db")
db = conn.cursor()
driver = webdriver.Safari()

#Logs into instagram
driver.get("https://www.instagram.com/accounts/login")
u = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
u.send_keys(uname)
p = driver.find_element_by_name("password")
p.send_keys("t")
sleep(1)
p.send_keys(Keys.TAB)
p.send_keys(Keys.BACKSPACE)
for i in password:
    p.send_keys(i)
    sleep(.2)
p.send_keys(Keys.RETURN)


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "TqC_a"))
)

driver.get("https://www.instagram.com/" + username)
try:
    assert username in driver.title
except AssertionError:
    print("Invalid Username")
    driver.quit()

WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.CLASS_NAME,"g47SY"))
)
fol = driver.find_element_by_xpath("//a[@href='/" + username +"/followers/']")
fol.click()


sleep(5)

#Checks if in database
isTable = db.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name = (?)", (username,)).fetchone()

if not isTable:
    db.execute("CREATE TABLE " + username + "(followerName VARCHAR(255));")
    conn.commit()

driver.quit()









