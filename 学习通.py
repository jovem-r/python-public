from selenium import webdriver
import time

accounts = input("请选择序号来登陆账号："
                 "\n序号0  用户A "
                 "\n序号1  用户B "
                 "\n序号2  用户C "
                 "\n序号3  用户D "
                 "\n序号4  重新输入账号，密码 ")

# 登录信息储存单元
if 0 <= int(accounts) < 1:
    account =  ''  # 账户
    passwoed = ''  # 密码
elif 1 <= int(accounts) < 2:
    account =  ''  # 账户
    passwoed = ''  # 密码
elif 2 <= int(accounts) < 3:
    account =  ''  # 账户
    passwoed = ''  # 密码
elif 3 <= int(accounts) < 4:
    account =  ''  # 账户
    passwoed = ''  # 密码
elif 4 <= int(accounts) < 5:
    account = input("请输入您的账号：")  # 账户
    passwoed = input("请输入您的密码：")  # 密码
else:
    print("请输入正确的序号")
# 刷课单选器
course = input("                  ！！！！！！！！！注意！！！！！！！！！！"
               "\n（选择课程数量时，请选择已经填入的课程，如果课程网址未填写且刷课，会出现程序停止的问题。）"
               "\n                  ！！！！！！！！！注意！！！！！！！！！！"
               "\n请选择需要刷的课程数量，请输入指定序号："
               "\n序号0  课程：AB "
               "\n序号1  课程：ABCD "
               "\n序号2  课程：ABCDEF "
               "\n序号3  课程：ABCDEFGH ")

# 课程网址
dict = {
 'a' : 'https://mooc2-ans.chaoxing.com/mooc2-ans/mycourse/stu?courseid=220017541&clazzid=82050074&cpi=266309580&enc=46655b6a5cd8a8f91434da6ac039d890&t=1694714189213&pageHeader=0&v=2',
 'b' : 'https://mooc2-ans.chaoxing.com/mooc2-ans/mycourse/stu?courseid=220017541&clazzid=62865638&cpi=266309580&enc=db0a10a0879f72816a3ea5c37ca574f0&t=1694714224666&pageHeader=0&v=2")',
 'c' : 'https://mooc2-ans.chaoxing.com/mooc2-ans/mycourse/stu?courseid=236648126&clazzid=81564957&cpi=266309580&enc=3923ff700791f2bdc170e5a845d1286f&t=1694966670675&pageHeader=1&v=2',
 'd' : 'https://mooc2-ans.chaoxing.com/mooc2-ans/mycourse/stu?courseid=236648116&clazzid=81564946&cpi=266309580&enc=5546479436f44a00d6a5e585cea97905&t=1694966698523&pageHeader=1&v=2',
 'e' : 'https://mooc2-ans.chaoxing.com/mooc2-ans/mycourse/stu?courseid=201593592&clazzid=81581124&cpi=266309580&enc=4c910dcdb9371949dc41eafa92fd05f0&t=1694962591348&pageHeader=0&v=2',
 'f' : 'https://mooc2-ans.chaoxing.com/mooc2-ans/mycourse/stu?courseid=229184846&clazzid=81580981&cpi=266309580&enc=c2e4678dddfcc478bad36fc4c0d4bdfb&t=1694962613053&pageHeader=0&v=2',
 'g' : '',
 'h' : '',
}

# 引用带插件的Firefox浏览器
fp = webdriver.FirefoxProfile(r'C:\Users\ren\AppData\Roaming\Mozilla\Firefox\Profiles\ild3xohq.default-release-1695102566212')
driver = webdriver.Firefox(fp)

# 登录单元
driver.get("http://zime.fanya.chaoxing.com/portal")
driver.implicitly_wait(10)
driver.find_element_by_css_selector('body > div.Header > div > div.Loginbefore > a.loginbtn').click()
driver.find_element_by_css_selector('#phone').send_keys(account)
driver.find_element_by_css_selector('#pwd').send_keys(passwoed)
driver.find_element_by_css_selector('#phoneLoginBtn').click()    #点击登录

# 进入刷课界面
driver.get("http://i.mooc.chaoxing.com/settings/info")
driver.find_element_by_css_selector('#zne_kc_icon > em').click()

# 进入刷课单元
driver.implicitly_wait(5)
driver.get(dict.get('a'))
if 0 <= int(course) < 1:                                                                                     # 刷2节课课程
    # 设置最大等待时间和循环次数
    max_wait_time = 86400  # 最大等待时间（单位：秒）    已设定24小时
    max_attempts = 8640  # 最大循环次数

    # 开始循环判断特定元素是否存在
    attempts = 0
    wait_time = 0

    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(dict.get('b'))
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环
elif 1 <= int(course) < 2:                                                                                   # 刷4节课课程
    # 设置最大等待时间和循环次数
    max_wait_time = 86400  # 最大等待时间（单位：秒）    已设定24小时
    max_attempts = 8640  # 最大循环次数

    # 开始循环判断特定元素是否存在
    attempts = 0
    wait_time = 0

    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(dict.get('b'))
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环
    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(dict.get('c'))
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环
    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(dict.get('d'))
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环
elif 2 <= int(course) < 3:                                                                                   # 刷6节课课程
    # 设置最大等待时间和循环次数
    max_wait_time = 86400  # 最大等待时间（单位：秒）    已设定24小时
    max_attempts = 8640  # 最大循环次数

    # 开始循环判断特定元素是否存在
    attempts = 0
    wait_time = 0

    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(dict.get('b'))
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环
    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(dict.get('c'))
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环
    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(dict.get('d'))
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环
    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(dict.get('e'))
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环
    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(dict.get('f'))
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环
elif 3 <= int(course) < 4:                                                                                   # 刷8节课课程
    # 设置最大等待时间和循环次数
    max_wait_time = 86400  # 最大等待时间（单位：秒）    已设定24小时
    max_attempts = 8640  # 最大循环次数

    # 开始循环判断特定元素是否存在
    attempts = 0
    wait_time = 0

    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(dict.get('b'))
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环
    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(dict.get('c'))
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环
    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(dict.get('d'))
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环
    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(dict.get('e'))
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环
    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(dict.get('f'))
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环
    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(dict.get('g'))
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环
    while wait_time < max_wait_time and attempts < max_attempts:
        try:
            element = driver.find_element_by_xpath("//*[contains(text(), '任务已全部完成')]")
            driver.get(dict.get('h'))
            break  # 如果成功找到特定文字，则跳出循环
        except:
            attempts += 1
            wait_time += 10  # 每次循环等待10秒
            time.sleep(10)  # 等待10秒后再执行下一次循环
else:
    print("请输入正确的序号")

# 回收内存
driver.quit()
print('学习通自动化脚本已执行完毕')
print(f"一共用时{wait_time}秒"
      f"\n循环检测{attempts}次")
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
