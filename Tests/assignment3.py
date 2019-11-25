import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_1_create_blog(self):
        user = "instructor"
        pwd = "maverick1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://kjanderson.pythonanywhere.com/admin/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://kjanderson.pythonanywhere.com")
        assert "Logged In"
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[1]/a/span").click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_title")
        elem.send_keys("This is a test post with selenium")
        elem = driver.find_element_by_id("id_text")
        elem.send_keys("This is a test post of text with selenium")
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/form/button").click()
        time.sleep(2)
        assert "Posted Blog Entry"
        driver.get("http://kjanderson.pythonanywhere.com")
        time.sleep(2)
        driver.get("http://kjanderson.pythonanywhere.com")

    def test_2_edit_blog(self):
        user = "instructor"
        pwd = "maverick1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://kjanderson.pythonanywhere.com/admin/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        assert "Logged In"
        time.sleep(2)

        elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/table/tbody/tr/th/a").click()
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[1]/th/a").click()

        new_title = "New Title from selenium test"
        new_text = "New text from selenium test."

        time.sleep(2)
        elem = driver.find_element_by_id("id_title")
        elem.clear()
        elem.send_keys(new_title)
        elem = driver.find_element_by_id("id_text")
        elem.clear()
        elem.send_keys(new_text)
        time.sleep(2)

        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()

        assert "Posted Blog Edited"
        driver.get("http://kjanderson.pythonanywhere.com")
        time.sleep(2)
        driver.get("http://kjanderson.pythonanywhere.com")

    def test_3_delete_blog(self):
        user = "instructor"
        pwd = "maverick1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://kjanderson.pythonanywhere.com/admin/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        assert "Logged In"
        time.sleep(2)

        elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/table/tbody/tr/th/a").click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[1]/th/a").click()
        time.sleep(2)

        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/p/a").click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/form/div/input[2]").click()
        time.sleep(2)

        assert "Posted Blog Deleted"
        driver.get("http://kjanderson.pythonanywhere.com")
        time.sleep(2)
        driver.get("http://kjanderson.pythonanywhere.com")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
