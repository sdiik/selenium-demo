# pages/page_base.py

print("✅ BasePage loaded")

class BasePage:
    def __init__(self, driver):
        self.driver = driver