import time
import random
#------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# NOTE: if for whatever reason you decided to use this program, or want to 
# develop new features make sure you have selenium webdriver installed
class InstaDriver():

    # initialize driver w username+password
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    # stop program from operating on its on
    def closeBrowser(self):
        driver = self.driver.close()

    # Takes user to ig.com and log in
    def login(self):
        url = 'http://www.instagram.com'
        self.driver.get(url)
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)
        self.driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']").click()
        time.sleep(1)
        input_user_name = self.driver.find_element_by_xpath("//input[@name='username']")
        input_user_name.send_keys(self.username)
        input_password = self.driver.find_element_by_xpath("//input[@name='password']")
        input_password.send_keys(self.password)
        input_password.send_keys(Keys.RETURN)
        time.sleep(2)

    # under development, main func of like_photo is to
    # scroll down to pictures and like random pictures
    # base on software's hashtag choice
    def like_photo(self,hashtag):
        self.driver.get('http://www.instagram.com/explore/tags/' + hashtag)
        time.sleep(1)
        # click and like each pic per row.
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        pic_elem = self.driver.find_element_by_class_name('_9AhH0').click()
        self.driver.find_elements_by_class_name('fr66n').click()

hashtags = [
        'ny','fashion','travel','california','newyork','style','gucci',
        'fashionnovamen','fashionnova','yeezy','traveler','softwareengineer',
        'programmer',
        ]
# IG User's logging inf
USERNAME = ''
PASSWORD = ''

go = InstaDriver(USERNAME,PASSWORD)
go.login()

random_htg = random.randint(0,len(hashtags))
while random_htg:
    go.like_photo(hashtags[random_htg])
