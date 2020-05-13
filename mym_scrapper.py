import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://mym.fans")

count = 0

print("Press any key when your are logged in and on the model page IN FEED VIEW...\n")
input()

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(0.5)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        print("Scrolling done\n")
        break
    print("Scrolling in progress")
    last_height = new_height

for photo in driver.find_elements_by_class_name('responsive-image'):
    src = photo.get_attribute('src')
    title = "downloaded_pictures_go_here/picture" + str(count) + ".jpeg"
    print(title + " downloaded successfully")
    urllib.request.urlretrieve(src, title)
    count+=1

print("\nJob done !")