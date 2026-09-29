username = input("用户名:")
password = input("密码:")

if username == "admin" and password == "123456":
    print("登录成功:")
elif username != "admin":
    print("用户名错误:")
else:
    print("密码错误:")