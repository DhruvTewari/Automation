from selenium import webdriver
import requests
import time
import os
import sys

path = 'path where you want your projects to be stored'

browser = webdriver.Chrome(r'Your chrome driver')
browser.get('https://github.com/login')

def create():

    email =  browser.find_element_by_name('login')
    email.send_keys('Your Email id for login')

    passw =  browser.find_element_by_xpath('//*[@id="password"]')
    passw.send_keys('your password')


    passw =  browser.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]')
    passw.click()

    time.sleep(2)
    add = browser.find_element_by_xpath('/html/body/div[1]/header/div[6]/details/summary')
    add.click()

    newrepo = browser.find_element_by_xpath('/html/body/div[1]/header/div[6]/details/details-menu/a[1]')
    newrepo.click()

    foldername = str(sys.argv[1])
    os.makedirs(path+'/' + foldername)

    namerepo = browser.find_element_by_xpath('//*[@id="repository_name"]')
    namerepo.send_keys(foldername)

    public_private = 'private'

    if len(sys.argv) == 3:
        public_private = str(sys.argv[2])

    if public_private == 'public':
        choice = browser.find_element_by_xpath('//*[@id="repository_visibility_public"]')
    else:
        choice = browser.find_element_by_xpath('//*[@id="repository_visibility_private"]')


    choice.click()

    submit = browser.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button')
    time.sleep(1)
    submit.click()
    time.sleep(2)
    browser.quit()



if __name__ == "__main__":
    # print(sys.argv)
    create()