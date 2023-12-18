import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from entity.commentDTO import Comment
import json
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from db.db_connect import comment_collection
from entity.commentModel import CommentModel


class Crawler:
    def __init__(self):
        # self.URL = "https://www.google.com/maps/place/%E4%B8%AD%E8%88%88%E5%A4%A7%E5%AD%B8%E7%B6%9C%E5%90%88%E6%95%99%E5%AD%B8%E5%A4%A7%E6%A8%93/@24.1222692,120.6721234,17z/data=!3m1!5s0x34693cfdf0f370f7:0xb5f97dcd8f1e9311!4m18!1m9!3m8!1s0x34693cfcecffe9d9:0xe28afadc0dad203a!2z5ZyL56uL5Lit6IiI5aSn5a24!8m2!3d24.123552!4d120.675326!9m1!1b1!16zL20vMDR4cDF6!3m7!1s0x34693cfdf13d560b:0xa4002a1f1219e2dd!8m2!3d24.1218109!4d120.6726999!9m1!1b1!16s%2Fg%2F11gvxx_g3b?entry=ttu"
        self.URL = ""
        self.service = webdriver.ChromeService(executable_path="./crawler/chromedriver/chromedriver")
        # self.service = webdriver.ChromeService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless")  # show browser or not
        self.options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(service=self.service, options=self.options)

    def get_data(self, driver):
        """
        this function get main text, score, name
        """
        print('################ get data')
        more_elements = driver.find_elements(by=By.CLASS_NAME, value='w8nwRe kyuRq')
        for list_more_element in more_elements:
            list_more_element.click()

        elements = driver.find_elements(by=By.CLASS_NAME, value='jftiEf')
        comment_data = []
        for ele in elements:
            try:
                comment = ele.find_element(by=By.CLASS_NAME, value='wiI7pd').text
            except:
                comment = ""

            name = ele.find_element(by=By.CLASS_NAME, value='d4r55').text
            score = ele.find_element(by=By.CLASS_NAME, value='kvMYJc').get_attribute("aria-label")
            score = score.split(' ')[0]
            comment_data.append(Comment(user_name=name, comment=comment, rating=score))

        return comment_data

    def counter(self):
        result = self.driver.find_element(by=By.CLASS_NAME, value="jANrlb").find_element(by=By.CLASS_NAME,
                                                                                         value="fontBodySmall").text
        result = result.split(' ')
        result = result[0].split('\n')
        print(f"result is {result}")
        return int(int(result[0]) / 10) + 1

    def scrolling(self, counter):
        print('################ scrolling')
        for _i in range(counter):
            scrolling = self.driver.execute_script(
                script='document.getElementsByClassName("dS8AEf")[0].scrollTop = document.getElementsByClassName("dS8AEf")[0].scrollHeight'
            )
            time.sleep(3)

    def fetch_comment(self, url: str = ''):
        if url == '':
            return 'Cannot Give Empty URL'

        self.URL = url
        self.driver.get(self.URL)
        time.sleep(5)

        counter = self.counter()
        self.scrolling(counter)

        comment_list = self.get_data(self.driver)
        self.driver.close()

        # for comment in comment_list:
        #     print(comment)

        print('Done!')

        comment_obj = CommentModel(comment=comment_list, url=url)

        comment_collection.insert_one(
            comment_obj.dict()
        )

        print(f"------------------- save to db done.")

        return comment_list

# if __name__ == "__main__":
# print('################ starting crawler')
# URL = "https://www.google.com/maps/place/%E4%B8%AD%E8%88%88%E5%A4%A7%E5%AD%B8%E7%B6%9C%E5%90%88%E6%95%99%E5%AD%B8%E5%A4%A7%E6%A8%93/@24.1222692,120.6721234,17z/data=!3m1!5s0x34693cfdf0f370f7:0xb5f97dcd8f1e9311!4m18!1m9!3m8!1s0x34693cfcecffe9d9:0xe28afadc0dad203a!2z5ZyL56uL5Lit6IiI5aSn5a24!8m2!3d24.123552!4d120.675326!9m1!1b1!16zL20vMDR4cDF6!3m7!1s0x34693cfdf13d560b:0xa4002a1f1219e2dd!8m2!3d24.1218109!4d120.6726999!9m1!1b1!16s%2Fg%2F11gvxx_g3b?entry=ttu"
# service = webdriver.ChromeService(executable_path="./chromedriver/chromedriver")
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # show browser or not
# options.add_argument("--no-sandbox")
# driver = webdriver.Chrome(service=service, options=options)

# driver.get(URL)
# time.sleep(5)
#
# counter = counter()
# scrolling(counter)
#
# comment_list = get_data(driver)
# driver.close()
#
# for comment in comment_list:
#     print(comment)
#
# print('Done!')
#
# # return comment_list
