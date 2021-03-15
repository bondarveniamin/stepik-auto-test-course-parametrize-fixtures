import time
def test_guest_should_see_button_add_to_basket(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    answer = browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket").text    
    time.sleep(30)
    assert len(answer) > 0    
    