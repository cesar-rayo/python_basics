from selenium import webdriver
import pytest

class TestSample():

    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="/media/cesar-rayo/948688348688193E/java/ubuntu/selenium/webdrivers/chromedriver_linux64/chromedriver")
        driver.implicitly_wait(30)
        driver.maximize_window()
        yield # Break
        driver.close() # close tab
        driver.quit() # close window
        print("Test ends")

    def test_navigation(self, test_setup):
        driver.get("https://luzavargas.github.io/supermercado/")
        driver.find_element_by_xpath('//*[@id="top_nav"]/ul/li[2]/a').click()
        driver.find_element_by_id("keyword").send_keys("Something")
        driver.find_element_by_id("searchbutton").click()
        assert driver.title == "Supermercados CRAI - Productos"
