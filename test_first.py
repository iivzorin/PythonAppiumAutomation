import pytest
from appium import webdriver

class TestFirst:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "AndroidTestDevice",
            "platformVersion": "8.0",
            "automationName": "Appium",
            "appPackage": "org.wikipedia",
            "appActivity": ".main.MainActivity",
            "app": "C:/Users/3217_plz/PycharmProjects/PythonAppiumAutomation/apks/org.wikipedia.apk"
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        yield

        self.driver.quit()

    def test_first(self):
        print("First test run")
