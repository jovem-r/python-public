import datetime
from selenium import webdriver
import time
import dict  # 个人dict.py文件引入

# 记录程序运行时间
start = datetime.datetime.now()
print("请选择序号来登陆账号："
      "\n序号0  用户A "
      "\n序号1  用户B "
      "\n序号2  用户C "
      "\n序号3  用户D "
      "\n序号4  重新输入账号，密码 ")

tag = 5
for i in range(1, 6):    # 五次输入错误机会
    accounts = input()
# 登录信息储存单元
    if 0 == int(accounts):
        account = dict.accounts["account"]  # 账户
        password = dict.accounts["password"]  # 密码
        print('Welcome %s login the system!' % account)
        break
    elif 1 == int(accounts):
        account = dict.accounts["account1"]  # 账户
        password = dict.accounts["password1"]  # 密码
        print('Welcome %s login the system!' % account)
        break
    elif 2 == int(accounts):
        account = dict.accounts["account2"]  # 账户
        password = dict.accounts["password2"]  # 密码
        print('Welcome %s login the system!' % account)
        break
    elif 3 == int(accounts):
        account = dict.accounts["account3"]  # 账户
        password = dict.accounts["password3"]  # 密码
        print('Welcome %s login the system!' % account)
        break
    elif 4 == int(accounts):
        account = input("请输入您的账号：")  # 账户
        password = input("请输入您的密码：")  # 密码
        print('Welcome %s login the system!' % account)
        break
    else:
        tag -= 1
        print(f"请输入正确的序号.\n您还有{tag}次机会")
        if tag == 0:
            print("用户名或密码错误！请联系后台管理员！")
            exit()

# 刷课单选器
print("                  ！！！！！！！！！注意！！！！！！！！！！"
      " \n（选择课程数量时，请选择已经填入的课程，如果课程网址未填写且刷课，会出现程序停止的问题。）"
      " \n                  ！！！！！！！！！注意！！！！！！！！！！"
      " \n请选择需要刷的课程数量，请输入指定序号："
      " \n序号0  课程：AB "
      " \n序号1  课程：ABCD "
      " \n序号2  课程：ABCDEF "
      " \n序号3  课程：ABCDEFGH ")
tags = 5
for courses in range(1, 6):   # 五次输入错误机会
    course = input()
    if 0 <= int(course) <= 3:
        course = int(course)
        break
    else:
        tags -= 1
        print(f"请输入正确的序号.\n您还有{tags}次机会！")
        if tags == 0:
            print("多次错误，请仔细核对序号输入！！！")
            exit()

# RE方式下获取的链接自己输入浏览器正常打开，可能是因为获取到了登录信息，但是webdriver方法下是指定浏览器链接
# 因此自动获取浏览器课程链接的方法宣告失败，这也是最后的一个版本了，我已经把可能出现的所有情况都写入其中，并且做出了相应的方法应对

# 课程网址
a = dict.url["a"]
b = dict.url["b"]
c = dict.url["c"]
d = dict.url["d"]
e = dict.url["e"]
f = dict.url["f"]
g = dict.url["g"]
h = dict.url["h"]

print("请选择序号来登陆账号："
      "\n序号0  正常浏览器 "
      "\n序号1  无头模式浏览器（正常带插件，在后台运行） ")
IE = 5
for i in range(1, 6):    # 五次输入错误机会
    accounts = input()
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

# 登录单元
driver.get("http://zime.fanya.chaoxing.com/portal")
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
driver.find_element_by_css_selector('body > div.Header > div > div.Loginbefore > a.loginbtn').click()
driver.find_element_by_css_selector('#phone').send_keys(account)
driver.find_element_by_css_selector('#pwd').send_keys(password)
driver.find_element_by_css_selector('#phoneLoginBtn').click()    # 点击登录

# 进入刷课界面
driver.get("http://i.mooc.chaoxing.com/settings/info")
driver.find_element_by_css_selector('#zne_kc_icon > em').click()

# 进入刷课单元
driver.implicitly_wait(5)
driver.get(a)

# 此处course判断函数为59行函数引用无需补全
if 0 == int(course):                                                                                     # 刷2节课课程
    # 设置最大等待时间和循环次数
    max_wait_time = 86400  # 最大等待时间（单位：秒）    已设定24小时
    max_attempts = 8640  # 最大循环次数

    # 开始循环判断特定元素是否存在
    attempts = 0
    wait_time = 0

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
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环

elif 1 == int(course):                                                                                   # 刷4节课课程
    # 设置最大等待时间和循环次数
    max_wait_time = 86400  # 最大等待时间（单位：秒）    已设定24小时
    max_attempts = 8640  # 最大循环次数

    # 开始循环判断特定元素是否存在
    attempts = 0
    wait_time = 0
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
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环

elif 2 == int(course):                                                                                   # 刷6节课课程
    # 设置最大等待时间和循环次数
    max_wait_time = 86400  # 最大等待时间（单位：秒）    已设定24小时
    max_attempts = 8640  # 最大循环次数

    # 开始循环判断特定元素是否存在
    attempts = 0
    wait_time = 0
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
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环

elif 3 == int(course):                                                                                   # 刷8节课课程
    # 设置最大等待时间和循环次数
    max_wait_time = 86400  # 最大等待时间（单位：秒）    已设定24小时
    max_attempts = 8640  # 最大循环次数

    # 开始循环判断特定元素是否存在
    attempts = 0
    wait_time = 0
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
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环
else:
    print("请输入正确的序号")

# 回收内存
driver.quit()
end = datetime.datetime.now()
print('学习通自动化脚本已执行完毕')
print(f"程序运行总时间:{end- start}"
      f"\n循环检测{attempts}次")
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
exit()
