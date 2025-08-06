import pytest
from pages.login_page import LoginPage
from testrail_reporter import add_result_for_case


def test_login_page_success(setup_driver):
    login_page = LoginPage(setup_driver)
    login_page.go_to()
    login_page.login("tohamindes@gmail.com", "Sukses111!!!")

    run_id = 17       # Ganti dengan Test Run ID aktif kamu
    case_id = 2389      # Ganti dengan Test Case ID di TestRail

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    try:
        login_page = LoginPage(setup_driver)
        login_page.go_to()
        login_page.login("tohamindes@gmail.com", "Sukses111!!!")

        WebDriverWait(setup_driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body")))

        home_headers = setup_driver.find_elements(By.XPATH, "//div[@aria-label='']")
        print("Jumlah header 'Home':", len(home_headers))
        for header in home_headers:
            print("Header ditemukan:", header.text)
            
        add_result_for_case(run_id, case_id, status_id=1, comment="Login success, header ditemukan")
    
    except Exception as e:
        print("❌ Test gagal:", str(e))
        add_result_for_case(run_id, case_id, status_id=5, comment=f"Login gagal: {str(e)}")
        raise  # tetap raise agar test dianggap fail oleh pytest