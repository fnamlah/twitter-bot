from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

TWITTER_USERNAME = "-"
TWITTER_PASSWORD = "-"

chrome_driver_path = Service("-")


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(service=chrome_driver_path)
        self.download = ""

    def get_internet_speed(self):
        self.driver.get("https://fast.com/")
        time.sleep(15)
        download = self.driver.find_element(By.XPATH, '//*[@id="speed-value"]').text
        self.download += download

    def tweet_at_provider(self):
        self.driver.get("https://www.twitter.com/i/flow/login")
        time.sleep(5)
        username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')

        username.send_keys(TWITTER_USERNAME)
        time.sleep(2)
        username.send_keys(Keys.ENTER)
        time.sleep(4)
        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(3)
        password.send_keys(Keys.ENTER)

        time.sleep(10)
        tweet_compose = self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-ltr')
        tweet_compose.send_keys(f"My download speed is {self.download} from STC")
        time.sleep(5)

        tweet_button = self.driver.find_element(By.XPATH, "//*[text()='Tweet']")
        tweet_button.click()


twitter_bot = InternetSpeedTwitterBot()
twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()

time.sleep(1000)

"""
echo "# workout-tracking" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git push -u origin main
"""