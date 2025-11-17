import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

EMAIL = "pythont758@gmail.com"
PASSWORD = 'A_nR.VgyW4B66js'
ACCOUNT = "chefsteps"



class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('https://www.instagram.com/')

    def login(self):
        time.sleep(15)
        email = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        email.send_keys(EMAIL)
        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        log_in = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button')
        log_in.click()
        time.sleep(15)
        try:
            save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
            if save_login_prompt:
                save_login_prompt.click()
            time.sleep(3.7)
        except:
            pass
        # Click "not now" on notifications prompt
        try:
            notifications_prompt = self.driver.find_element(by=By.XPATH, value="// button[contains(text(), 'Not Now')]")
            if notifications_prompt:
                notifications_prompt.click()
        except:
            pass

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{ACCOUNT}/")
        followers = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, '//a[contains(@href, "/followers")]/span')
            )
        )
        print(followers.text)
        followers.click()

        modal = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']"))
        )

        # wait for scrollable container inside modal
        scroll_box = WebDriverWait(modal, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//div[@class='isgrP']"))
        )

        # scroll safely
        for _ in range(5):
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", scroll_box
            )
            time.sleep(2)

    def follow(self):
        people = self.driver.find_elements(By.XPATH, '/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[3]/div/button')
        for i in people:
            try:
                i.click()
                time.sleep(1.1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()

time.sleep(60)
bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
