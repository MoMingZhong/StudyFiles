from selenium import webdriver

driver=webdriver.Firefox()
driver.get('http://www.santostang.com/2018/07/04/hello-world/')
driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere-comment']"))
comments=driver.find_elements_by_css_selector('div.reply-content')
for comment in comments:
    content=comment.find_element_by_tag_name('p')
    print(content.text)