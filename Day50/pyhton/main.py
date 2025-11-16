import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PROMISED_DOWN = 150
PROMISED_UP = 10

class InternetSpeedTwitterBot:
    def __init__(self):

        options = webdriver.ChromeOptions()
        options.add_argument("--user-data-dir=C:/SeleniumProfile")
        options.add_argument("--profile-directory=Default")

        options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=options)

        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "start-text")))
        go_button.click()
        time.sleep(30)
        download_speed = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "download-speed")))
        self.down = download_speed.text
        time.sleep(30)
        upload_speed = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "upload-speed")))
        self.up = upload_speed.text

    def tweet_at_provider(self):
        self.driver.get("https://x.com")
        time.sleep(5)
        input_form = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        input_form.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when i pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        post = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')
        post.click()

internet_speed = InternetSpeedTwitterBot()
internet_speed.get_internet_speed()
print(internet_speed.up)
print(internet_speed.down)
internet_speed.tweet_at_provider()

