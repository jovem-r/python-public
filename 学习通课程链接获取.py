from selenium import webdriver
import time
import re

account = ''  # 账户
password = ''  # 密码

option = webdriver.FirefoxOptions()
option.add_argument("--headless")
driver = webdriver.Firefox(options=option)
f = open('学习通课程链接.csv', mode="w", encoding='utf-8')
driver.get("http://zime.fanya.chaoxing.com/portal")
driver.find_element_by_css_selector('body > div.Header > div > div.Loginbefore > a.loginbtn').click()
driver.find_element_by_css_selector('#phone').send_keys(account)
driver.find_element_by_css_selector('#pwd').send_keys(password)
driver.find_element_by_css_selector('#phoneLoginBtn').click()    # 点击登录
driver.get("http://i.mooc.chaoxing.com/settings/info")
driver.find_element_by_css_selector('#zne_kc_icon > em').click()
driver.implicitly_wait(10)
driver.switch_to.frame("frame_content")
time.sleep(3)
html_code = driver.page_source
href_list = re.findall(r'<a href=".*?(?P<href>.*?)" target="_blank"', html_code)

for href in href_list:
    print(href)
    f.write(f"{href}\n")
driver.quit()
# RE方式下获取的链接自己输入浏览器正常打开，可能是因为获取到了登录信息，但是webdriver方法下是指定浏览器链接
# 因此自动获取浏览器课程链接的方法宣告失败