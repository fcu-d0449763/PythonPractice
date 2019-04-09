# HW4
a = input()
supper = False
num = False
lower = False
for i in a:
    if i.isupper():
        supper = True
    if i.isnumeric():
        num = True
    if i.islower():
        lower = True
if supper and num and lower:
    print("密碼設定完成")
else:
    print("密碼設定不符合規定")