# s = input("一共有多少个月饼:")
# a = input("每个盒子放多少月饼:")
# boxNum = int(s) // int(a)
# print(f"一共可以装{boxNum}盒")
# left = int(s) % int(a)
# print(f"还剩下{left}个")

weight = input("请输入你的体重(kg)")
height = input("请输入你的身高(m)")
BMI = float(weight)/(float(height)*float(height))
print(f"您的BMI值为{BMI}")
if BMI > 24.9:
    print("您的体重过重，请注意身体，增加锻炼")
elif BMI < 18.5:
    print("您的体重过轻，需要增加饮食")
else:
    print("您的体重正常，请继续保持")
