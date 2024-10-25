from selenium import webdriver


class infow:
    def __init__(self):
        # Initialize webdriver, assuming using Chrome
        self.driver = webdriver.Chrome()

    def get_info(self, query):
        self.driver.get(f"https://en.wikipedia.org/wiki/{query}")
        # Simulate more actions based on your requirements

    def close(self):
        self.driver.quit()
