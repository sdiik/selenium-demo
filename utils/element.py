from selenium.webdriver.common.by import By

def get_button(driver, button_id):
    try:
        return driver.find_element(By.ID, button_id)
    except Exception as e:
        print(f"Error finding button with ID {button_id}: {e}")
        return None
    


def get_input_field(driver, field_id):
    try:
        return driver.find_element(By.ID, field_id)
    except Exception as e:
        print(f"Error finding input field with ID {field_id}: {e}")
        return None