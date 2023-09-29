# s = input("一共有多少个月饼:")
# a = input("每个盒子放多少月饼:")
# boxNum = int(s) // int(a)
# print(f"一共可以装{boxNum}盒")
# left = int(s) % int(a)
# print(f"还剩下{left}个")

# weight = input("请输入你的体重(kg)")
# height = input("请输入你的身高(m)")
# BMI = float(weight)/(float(height)*float(height))
# print(f"您的BMI值为{BMI}")
# if 24 < BMI <= 28:
#     print("您的体重过重，请注意身体，增加锻炼")
# elif BMI <= 18.5:
#     print("您的体重过轻，需要增加饮食")
# elif 28 < BMI <= 32:
#     print("您的体重严重过重，请注意身体")
# elif 32 < BMI:
#     print("严重肥胖，请注意身体")
# else:
#     print("您的体重正常，请继续保持")


# a = 495
# b = 660
# c = 825
# _c = int(c)*int(c)
# shuzi = int(a)*int(a)+int(b)*int(b)
# if _c == shuzi:
#     print("这个是直角三角形")
# else:
#     print("不是直角三角形")


# age = 20
# height = 175
# if 17 <= age <= 27 and 169 <= height <= 185:
#     print("符合条件")
# else:
#     print("不符合条件")


# citypopulation = 10 # 单位万
# if 5 >= citypopulation:
#     print("small city")
# elif 5 < citypopulation <= 40:
#     print("middle city")
# else:
#     print("big city")

num = 98
if 0 < num <= 100:
    if num % 2 == 0:
        print("偶数")
    else:
        print("不是偶数")
else:
    print("不是偶数")

# skill = 110
# click = 1
# if skill >= 100:
#     print("大招准备就绪")
#     if click == 1:
#         print("大招已发送")
#     else:
#         print("大招未发送")

# year = 1900
# if year // 4 == 0 and year // 100 == 0 or not year // 400 == 0:
#     print("闰年")
# else:
#     print("不是闰年")
