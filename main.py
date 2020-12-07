import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


url = 'http://projectby.trainings.dlabanalytics.com/kkochav804/tree?'
username = ''
password = ''


def found_window(windows_before, windows_after):
    for window in windows_after:
        if window not in windows_before:
            return window


browser = webdriver.Chrome()
browser.implicitly_wait(50)
browser.get(url)
browser.find_element_by_id('details-button').click()
browser.find_element_by_id('proceed-link').click()
browser.find_element_by_id('zocial-epam-idp').click()
browser.find_element_by_id('userNameInput').send_keys(username)
browser.find_element_by_id('passwordInput').send_keys(password)
browser.find_element_by_id('submitButton').click()
windows_before = browser.window_handles
browser.find_element_by_xpath("//*[@id='notebook_list']//a[contains(@href,'Untitled.ipynb')]").click()
title = "Untitled - Jupyter Notebook"
WebDriverWait(browser, 20).until(
    lambda driver: len(windows_before) != len(driver.window_handles)) and title in browser.window_handles

browser.switch_to.window(found_window(windows_before, browser.window_handles))
WebDriverWait(browser, 20).until(
    lambda driver: browser.find_element_by_xpath("//a[text()='Cell']").is_displayed())

browser.find_element_by_xpath("//a[text()='Cell']").click()

time.sleep(3)

browser.find_element_by_id('run_all_cells').click()

WebDriverWait(browser, 20).until(
    lambda driver: browser.find_element_by_xpath("//pre[contains(text(),'Done!')]").is_displayed())

browser.quit()