import datetime
from selenium import webdriver
import time
import re
import ast
from selenium.webdriver.firefox.options import Options
import random

# 记录程序运行时间
start = datetime.datetime.now()
def read_account_info(filename):
    with open(filename, 'r') as file:
        content = file.read()
        account_info = ast.literal_eval(content)  # 将文本内容转换为字典
    return account_info

# 输出账户列表并获取用户选择的序号
def select_account(account_info, max_tries=5):
    for i in range(max_tries):
        print('可选账户列表：')
        for j, account in enumerate(account_info.keys()):
            print(f'{j+1}. {account}')
        index = input('请选择账户序号：')
        if index.isdigit() and int(index) <= len(account_info):
            return list(account_info.keys())[int(index)-1]
        else:
            print(f'输入错误，请重新输入。你还有{max_tries - i - 1}次机会。\n')
    print(f'程序退出。你已经连续输入错误{max_tries}次。')
    exit(1)
# 登录流程
filename = 'account.txt'
account_info = read_account_info(filename)
account = select_account(account_info)
password = account_info[account]
print('Welcome %s login the system!' % account)


print("正在获取课程信息，请稍后。。。。。")
# 获取课程网址
# 设置Firefox浏览器选项
firefox_options = Options()
firefox_options.headless = True
# 创建WebDriver对象
driver = webdriver.Firefox(options=firefox_options)
# 使用随机的用户代理
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.40",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
]
user_agent = random.choice(user_agents)
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", user_agent)
driver = webdriver.Firefox(firefox_profile=profile, options=firefox_options)
# 登录
driver.get("https://passport2.chaoxing.com/login?fid=&newversion=true&refer=https://i.chaoxing.com")
driver.find_element_by_css_selector('#phone').send_keys(account)
driver.find_element_by_css_selector('#pwd').send_keys(password)
driver.find_element_by_css_selector('#loginBtn').click()
driver.implicitly_wait(10)
# 切换到iframe
driver.switch_to.frame(driver.find_element_by_css_selector("iframe[name=\"frame_content\"]"))
# 获取课程链接和名称
html_code = driver.page_source
href_list = re.findall(r'<li class="course clearfix".*? id="(?P<href>.*?)">', html_code, re.S)
name = re.findall(r'<span class="course-name overHidden2" title=".*?">(?P<href>.*?)</span>', html_code, re.S)
# 访问课程链接并获取URL
course_urls = []
for index, href in enumerate(href_list[:8]):
    driver.find_element_by_css_selector(f"#{href} div").click()
    all_handles = driver.window_handles
    driver.switch_to.window(all_handles[-1])
    time.sleep(random.uniform(2, 4))  # 添加随机延迟
    course_urls.append(driver.current_url)
    driver.close()
    driver.switch_to.window(all_handles[0])
    driver.switch_to.frame(driver.find_element_by_css_selector("iframe[name=\"frame_content\"]"))
for i, course_name in enumerate(name[:8]):
    print(f"{i+1}. {course_name}")
# 将URL赋值给abcdefgh这八个变量
a, b, c, d, e, f, g, h = course_urls
driver.quit()

# 刷课单选器
print(" 请选择需要刷的课程数量，请输入指定序号："
      " \n序号0  课程：1-2 "
      " \n序号1  课程：1-4 "
      " \n序号2  课程：1-6 "
      " \n序号3  课程：1-8 ")
tags = 5
for courses in range(1, 6):   # 五次输入错误机会
    course = input("请输入序号：")
    if 0 <= int(course) <= 3:
        course = int(course)
        break
    else:
        tags -= 1
        print(f"请输入正确的序号.\n您还有{tags}次机会！")
        if tags == 0:
            print("多次错误，请仔细核对序号输入！！！")
            exit()



print("请选择序号来登陆账号："
      "\n序号0  正常浏览器 "
      "\n序号1  无头模式浏览器（正常带插件，在后台运行） ")
IE = 5
for i in range(1, 6):    # 五次输入错误机会
    accounts = input("请输入序号：")
# 登录信息储存单元
    if 0 == int(accounts):
        # 引用带插件的Firefox浏览器                       请自行修改自己的Firefox浏览器配置文件路径，否则会出现无法打开带插件的浏览器
        fp = webdriver.FirefoxProfile(r'C:\Users\ren\AppData\Roaming\Mozilla\Firefox\Profiles\ild3xohq.default-release-1695102566212')
        driver = webdriver.Firefox(fp)
        break
    elif 1 == int(accounts):
        # 引用无头模式带插件的Firefox浏览器
        firefox_options = webdriver.FirefoxOptions()
        # 启用无头模式
        firefox_options.add_argument("--headless")
        # 设置个人配置路径
        firefox_options.profile = r'C:\Users\ren\AppData\Roaming\Mozilla\Firefox\Profiles\ild3xohq.default-release-1695102566212'
        # 创建一个WebDriver对象，指定Firefox浏览器驱动程序和选项
        driver = webdriver.Firefox(options=firefox_options)
        break
    else:
        IE -= 1
        print(f"请输入正确的序号.\n您还有{IE}次机会！")
        if IE == 0:
            print("多次错误，请仔细核对序号输入！！！")
            exit()
print("程序运行中。。。。请勿关闭！！！！！！！！")
# 登录单元
driver.get("https://passport2.chaoxing.com/login?fid=&newversion=true&refer=https://i.chaoxing.com")
driver.implicitly_wait(10)
# 获取全部页面句柄
all_handles = driver.window_handles
# 将当前句柄定位到新打开的页面
driver.switch_to.window(all_handles[-1])
# 关闭脚本猫提示网页
driver.close()
# 定位学习通网页
driver.switch_to.window(all_handles[0])
driver.implicitly_wait(10)
# 登录单元
driver.find_element_by_css_selector('#phone').send_keys(account)
driver.find_element_by_css_selector('#pwd').send_keys(password)
driver.find_element_by_css_selector('#loginBtn').click()    # 点击登录

# 进入刷课单元
driver.implicitly_wait(5)
driver.get(a)
print("正在刷第一节课。。。")
# 设置最大等待时间和循环次数
max_wait_time = 86400  # 最大等待时间（单位：秒）    已设定24小时
max_attempts = 8640  # 最大循环次数

# 开始循环判断特定元素是否存在
attempts = 0
wait_time = 0

# 此处course判断函数为63行函数引用无需补全
if 0 == int(course):                                                                                     # 刷2节课课程
    # 设定时间上午七点三十分刷新浏览器，防止出现学习通学习记录失效的问题！！！！！！
    times = datetime.time(7, 30)
    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            # 获取当前时间，对比是否到达设定时间
            timess = datetime.datetime.now().time()
            if times.hour == timess.hour and times.minute == timess.minute:
                driver.refresh()
                print("防止学习记录无效，已刷新浏览器")
            else:
                pass
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(b)
            print("正在刷第二节课。。。")
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环

elif 1 == int(course):                                                                                   # 刷4节课课程
    times = datetime.time(7, 30)
    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            timess = datetime.datetime.now().time()
            if times.hour == timess.hour and times.minute == timess.minute:
                driver.refresh()
                print("防止学习记录无效，已刷新浏览器")
            else:
                pass
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(b)
            print("正在刷第二节课。。。")
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环
    times = datetime.time(7, 30)
    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            timess = datetime.datetime.now().time()
            if times.hour == timess.hour and times.minute == timess.minute:
                driver.refresh()
                print("防止学习记录无效，已刷新浏览器")
            else:
                pass
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(c)
            print("正在刷第三节课。。。")
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环
    times = datetime.time(7, 30)
    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            timess = datetime.datetime.now().time()
            if times.hour == timess.hour and times.minute == timess.minute:
                driver.refresh()
                print("防止学习记录无效，已刷新浏览器")
            else:
                pass
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(d)
            print("正在刷第四节课。。。")
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环

elif 2 == int(course):                                                                                   # 刷6节课课程
    times = datetime.time(7, 30)
    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            timess = datetime.datetime.now().time()
            if times.hour == timess.hour and times.minute == timess.minute:
                driver.refresh()
                print("防止学习记录无效，已刷新浏览器")
            else:
                pass
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(b)
            print("正在刷第二节课。。。")
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环
    times = datetime.time(7, 30)
    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            timess = datetime.datetime.now().time()
            if times.hour == timess.hour and times.minute == timess.minute:
                driver.refresh()
                print("防止学习记录无效，已刷新浏览器")
            else:
                pass
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(c)
            print("正在刷第三节课。。。")
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环
    times = datetime.time(7, 30)
    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            timess = datetime.datetime.now().time()
            if times.hour == timess.hour and times.minute == timess.minute:
                driver.refresh()
                print("防止学习记录无效，已刷新浏览器")
            else:
                pass
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(d)
            print("正在刷第四节课。。。")
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环
    times = datetime.time(7, 30)
    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            timess = datetime.datetime.now().time()
            if times.hour == timess.hour and times.minute == timess.minute:
                driver.refresh()
                print("防止学习记录无效，已刷新浏览器")
            else:
                pass
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(e)
            print("正在刷第五节课。。。")
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环
    times = datetime.time(7, 30)
    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            timess = datetime.datetime.now().time()
            if times.hour == timess.hour and times.minute == timess.minute:
                driver.refresh()
                print("防止学习记录无效，已刷新浏览器")
            else:
                pass
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(f)
            print("正在刷第六节课。。。")
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环

elif 3 == int(course):                                                                                   # 刷8节课课程
    times = datetime.time(7, 30)
    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            timess = datetime.datetime.now().time()
            if times.hour == timess.hour and times.minute == timess.minute:
                driver.refresh()
                print("防止学习记录无效，已刷新浏览器")
            else:
                pass
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(b)
            print("正在刷第二节课。。。")
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环
    times = datetime.time(7, 30)
    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            timess = datetime.datetime.now().time()
            if times.hour == timess.hour and times.minute == timess.minute:
                driver.refresh()
                print("防止学习记录无效，已刷新浏览器")
            else:
                pass
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(c)
            print("正在刷第三节课。。。")
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环
    times = datetime.time(7, 30)
    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            timess = datetime.datetime.now().time()
            if times.hour == timess.hour and times.minute == timess.minute:
                driver.refresh()
                print("防止学习记录无效，已刷新浏览器")
            else:
                pass
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(d)
            print("正在刷第四节课。。。")
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环
    times = datetime.time(7, 30)
    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            timess = datetime.datetime.now().time()
            if times.hour == timess.hour and times.minute == timess.minute:
                driver.refresh()
                print("防止学习记录无效，已刷新浏览器")
            else:
                pass
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(e)
            print("正在刷第五节课。。。")
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环
    times = datetime.time(7, 30)
    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            timess = datetime.datetime.now().time()
            if times.hour == timess.hour and times.minute == timess.minute:
                driver.refresh()
                print("防止学习记录无效，已刷新浏览器")
            else:
                pass
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(f)
            print("正在刷第六节课。。。")
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环
    times = datetime.time(7, 30)
    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            timess = datetime.datetime.now().time()
            if times.hour == timess.hour and times.minute == timess.minute:
                driver.refresh()
                print("防止学习记录无效，已刷新浏览器")
            else:
                pass
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(g)
            print("正在刷第七节课。。。")
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环
    times = datetime.time(7, 30)
    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            timess = datetime.datetime.now().time()
            if times.hour == timess.hour and times.minute == timess.minute:
                driver.refresh()
                print("防止学习记录无效，已刷新浏览器")
            else:
                pass
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(h)
            print("正在刷第八节课。。。")
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环
else:
    print("请输入正确的序号")

times = datetime.time(7, 30)
while wait_time < max_wait_time and attempts < max_attempts:
    try:
        timess = datetime.datetime.now().time()
        if times.hour == timess.hour and times.minute == timess.minute:
            driver.refresh()
            print("防止学习记录无效，已刷新浏览器")
        else:
            pass
        element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
        break  # 如果成功找到特定文字，则跳出循环
    except:
        attempts += 1
        wait_time += 10  # 每次循环等待10秒
        time.sleep(10)  # 等待10秒后再执行下一次循环

# 回收内存
driver.quit()
end = datetime.datetime.now()
print('学习通自动化脚本已执行完毕')
print(f"程序运行总时间:{end- start}"
      f"\n循环检测{attempts}次")
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
exit()
