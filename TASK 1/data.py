from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
browser = webdriver.Chrome(service=Service(executable_path="D:/drivers/chromedriver-win64/chromedriver.exe"))
def getinfo(question):
    browser.get("https://logicballs.com/tools/question-and-answer-generator#:~:text=Questions%20and%20Answers%20Generator,find%20the%20information%20you%20need.")
    browser.find_element(By.CSS_SELECTOR, "#topic").send_keys(question)
    browser.find_element(By.CSS_SELECTOR, "#btn-submit").click()
    time.sleep(10)
    answer=browser.find_element(By.XPATH, "/html/body/main/section/div/div/div[2]/div/div/div/form/div[2]/div/div[2]/div").text
    return answer
def playsong(song):
     browser.get("https://wynk.in/music/search")
     browser.find_element(By.CSS_SELECTOR, "input.sm\:block").send_keys(song)
     time.sleep(5)
     browser.find_element(By.CSS_SELECTOR, ".zapSearch_zapSearchList__TvGT1 > div:nth-child(1) > a:nth-child(1)").click()
     time.sleep(500)
def playvideo(video):
    browser.get("https://www.youtube.com/")
    browser.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").send_keys(video)
    browser.find_element(By.XPATH, "//*[@id='search-icon-legacy']").click()
    time.sleep(5)
    browser.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a").click()
    time.sleep(500)
def showphotos(photo):
    browser.get("https://www.google.com/")
    browser.find_element(By.CSS_SELECTOR, "#APjFqb").send_keys(photo)
    browser.find_element(By.CSS_SELECTOR, "#APjFqb").send_keys(Keys.ENTER)
    try:
        time.sleep(10)
        browser.find_element(By.CSS_SELECTOR, "#hdtb-sc > div > div > div.zp6Lyf.FpfXM > div.IUOThf > a:nth-child(2)").click()
    except Exception as e:
        print()
    time.sleep(100)