#HW02_3
myDic = {'cat':'貓','dog':'狗'}
while 1:
    choice = input("請輸入選項(1)英翻中(2)中翻英(3)離開：")
    if choice =='1':
        question = input("請輸入英文單字：")
        if myDic.get(question):
            print(myDic.get(question))
        else:
            print("查無此單字")
    elif choice =='2':
        question = input("請輸入中文單字：")
        if question in list(myDic.values()):
            print(list(myDic.keys())[list(myDic.values()).index(question)])
        else:
            print("查無此單字")
    elif choice =='3':
        break
    else:
        print("無此選項")
