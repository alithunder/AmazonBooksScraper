# import libraries

import requests
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from amazoncaptcha import AmazonCaptcha
#
# first codes
searchbarr = f" {input()}"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.amazon.com/")
time.sleep(60)
search = driver.find_element(By.ID, "twotabsearchtextbox")
search.send_keys(searchbarr)
search.send_keys(Keys.RETURN)
cata = driver.find_element(By.XPATH , "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[1]/div/div/select")
cata.click()
catas = driver.find_element(By.XPATH , "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[1]/div/div/select/option[6]")
catas.click()
icon = driver.find_element(By.XPATH , "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div")
icon.click()
# first item
link = driver.find_element(By.CLASS_NAME , "s-image")
link.click()
link2 = driver.find_element(By.XPATH, "//a[text()='See this image']")
link2.click()
popup_img = driver.find_element(By.ID, "igImage")
popup_img_src = popup_img.get_attribute("src")

response = requests.get(popup_img_src)

if response.status_code == 200:
    image_data = response.content

    with open(f"images/{searchbarr}.jpg", "wb") as f:
        f.write(image_data)

    print("Image downloaded successfully.")
else:
    print("Failed to download image. Status code:", response.status_code)

# second item
driver.back()
link3 = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img")
link3.click()
link4 = driver.find_element(By.XPATH, "//a[text()='See this image']")
link4.click()
popup_img = driver.find_element(By.ID, "igImage")
popup_img_src = popup_img.get_attribute("src")

response = requests.get(popup_img_src)

if response.status_code == 200:
    image_data = response.content

    with open(f"C:/Users/Thunder/PycharmProjects/Myamazonscraper/images/{searchbarr}-2.jpg", "wb") as f:
        f.write(image_data)

    print("Image downloaded successfully.")
else:
    print("Failed to download image. Status code:", response.status_code)

# third item
driver.back()
link5 = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img")
link5.click()
link4 = driver.find_element(By.XPATH, "//a[text()='See this image']")
link4.click()
popup_img = driver.find_element(By.ID, "igImage")
popup_img_src = popup_img.get_attribute("src")

response = requests.get(popup_img_src)

if response.status_code == 200:
    image_data = response.content

    with open(f"C:/Users/Thunder/PycharmProjects/Myamazonscraper/images/{searchbarr}-3.jpg", "wb") as f:
        f.write(image_data)

    print("Image downloaded successfully.")
else:
    print("Failed to download image. Status code:", response.status_code)


