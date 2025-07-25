def test_profile_page_success(logged_in_driver):
    driver = logged_in_driver
    driver.get("https://www.facebook.com/profile")
    assert "Facebook" in driver.title