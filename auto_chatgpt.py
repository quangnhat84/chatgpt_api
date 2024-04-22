#======================================
#coded by helios.zayden
#the xpaths were taken on 2024/04/21 
#
#======================================

import config
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

#ref : https://github.com/0ut0flin3
import undetected_chromedriver as uc
from fake_useragent import UserAgent
op = webdriver.ChromeOptions()
op.add_argument(f"user-agent={UserAgent.random}")
op.add_argument("user-data-dir=./")
op.add_experimental_option("detach", True)
op.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = uc.Chrome(chrome_options=op)

#Confirm is Logged in ChatGPT or not.
def isLoggedIn():
    try:
        driver.find_element(By.ID, 'headlessui-menu-button-:rb:')
        print('Log-in')
        return True
    except NoSuchElementException:
        print('Not yet log-in')
        return False
    
#Open ChatGPT page
def open_chatGPT():
    driver.get('https://chat.openai.com/')
    time.sleep(5)

#Open ChatGPT page and login
def open_login_chatGPT(MAIL,PASSWORD):
    
    open_chatGPT()

    if isLoggedIn():
        return
    
    #click on Login button
    loginButton = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div/nav/div[2]/div[2]/button[2]/div')
    loginButton.click()
    time.sleep(5) #wait to direct to login page

    #input email into email field
    mail = driver.find_element(By.ID,'email-input')
    mail.send_keys(MAIL)
    #click continue button
    continueBtn=driver.find_element(By.XPATH,'/html/body/div/div/main/section/div[2]/button')
    continueBtn.click()
    time.sleep(5)

    #input pwd into pwd field
    password= driver.find_element(By.ID,'password')
    password.send_keys(PASSWORD)
    #click continue button
    continueBtn=driver.find_element(By.XPATH, '/html/body/div[1]/main/section/div/div/div/form/div[2]/button')
    continueBtn.click()
    time.sleep(10) #wait to process login
    
def get_chatGPT_response(prompt):
    messageBox = driver.find_element(By.ID, 'prompt-textarea')
    messageBox.send_keys(prompt)
    time.sleep(1)
    messageBox.send_keys(Keys.RETURN)
    time.sleep(10)

    replies = driver.find_elements(By.XPATH, "//div[@data-message-author-role='assistant']")
    response = ""
    for reply in replies:
        print(reply.text)
        response = reply.text

    time.sleep(5)
    return response
    
def get_10_click_worthy_titles():
    open_chatGPT()
    #open_login_chatGPT(config.chatGPT['email'],config.chatGPT['pwd'])
    prompt = config.worthyPrompt['prompt1']
    response=get_chatGPT_response(prompt)
    print(response)

def get_1000_blog_content():
    open_chatGPT()
    #open_login_chatGPT(config.chatGPT['email'],config.chatGPT['pwd'])
    prompt = config.blogPrompt['prompt1']
    response=get_chatGPT_response(prompt)
    print(response)

get_10_click_worthy_titles()
driver.close()