import chromedriver_binary
# import lxml
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests

# base_url = "https://www.104.com.tw/jobs/search/?keyword=%E7%88%AC%E8%9F%B2%E5%B7%A5%E7%A8%8B%E5%B8%AB&order=1&jobsource=2018indexpoc&ro=0"


def url_updater():

    name_of_vacancy = str(input())

    browser = webdriver.Chrome()
    browser.maximize_window()

    browser.get("https://www.104.com.tw/jobs/main/")
    searcher = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, "ikeyword")))
    searcher.send_keys(name_of_vacancy)
    searcher_button = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button.btn.btn-primary.js-formCheck')))
    searcher_button.click()

    fulltime_css = "#js-job-tab > li:nth-child(2)"
    fulltime = browser.find_element(By.CSS_SELECTOR, fulltime_css)
    tot_num = fulltime.text.replace(")", "").replace("(", "")
    fulltime.click()
    base_url = browser.current_url

    sleep(10)

    browser.close()

    return base_url


def get_html():

    # url_for_search = 'https://www.104.com.tw/jobs/search/?keyword=%E7%88%AC%E8%9F%B2%E5%B7%A5%E7%A8%8B%E5%B8%AB&order=1&jobsource=2018indexpoc&ro=0'

    url_for_search = url_updater()

    headers = {"User-Agent": "ILOVETAIWAN/2.0 (EVM x8), CurlyLegs40/1;p"}

    s = requests.Session()
    s.headers.update(headers)

    response = requests.get(url_for_search, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    all_vac = soup.find_all("article", class_="b-block--top-bord job-list-item b-clearfix js-job-item")

    for i in all_vac:
        yield i


def main_scraper():

    for _ in get_html():
        publication = _.find("span", class_="b-tit__date").text.replace("'", "")
        vac_name = _.get("data-job-name").replace(" ", "")
        vac_company = _.get("data-cust-name").replace(" ", "")

        link = _.find("a", class_="js-job-link").get("href")[2:]

        try:
            vac_loc = \
            _.find("ul", class_="b-list-inline b-clearfix job-list-intro b-content").text.replace("'", "").replace(" ",
                                                                                                                   "").split(
                "\n")[1]
        except:
            vac_loc = '無訊息'

        try:
            vac_exp = \
            _.find("ul", class_="b-list-inline b-clearfix job-list-intro b-content").text.replace("'", "").replace(" ",
                                                                                                                   "").split(
                "\n")[3]
        except:
            vac_exp = '無訊息'

        try:
            people = _.find("a", class_="b-link--gray gtm-list-apply").text.replace(" ", "")
        except:
            people = '無訊息'

        try:
            duty = _.find("p", class_="job-list-item__info b-clearfix b-content").text
        except:
            duty = '無訊息'

        yield vac_name, publication, vac_company, vac_loc, vac_exp, people, duty, link




        # print(f"Vacancy N{all_vac.index(_)}")
        # print(publication, "\n", vac_name, "\n", vac_company, "\n", vac_loc, "\n", vac_exp, "\n", people, "\n", duty)





"""
        try:
            vac_salary = _.find_all("a", class_="b-tag--default")[0].text
        except:
            vac_salary = "無訊息"

        try:
            tot_employees = _.find_all("a", class_="b-tag--default")[1].text
        except:
            tot_employees = "無訊息"
"""