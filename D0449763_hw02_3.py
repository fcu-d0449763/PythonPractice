#HW02_4
pokemon = {
    '1':('皮卡丘',0.4,6.0,'靜電','雄','電'),
    '2':('伊布',0.3,6.5,'適應力','雌','一般'),
    '3':('六尾',0.6,9.9,'引火','雌','火'),
    '4':('九尾',1.1,19.9,'引火','雌','火'),
    '5':('菊草葉',0.9,6.4,'茂盛','雄','草'),
    '6':('噴火龍',1.7,90.5,'猛火','雄','火'),
    '7':('傑尼龜',0.5,9.0,'激流','雄','水'),
    '8':('木守宮',0.5,5.0,'茂盛','雄','草'),
    '9':('小火龍',0.6,8.5,'猛火','雄','火')
}

def pokemonformat(k,v):
    print("編號:{}\t名稱:{:^3s}\t身高:{}m\t體重:{}kg\t特性:{}\t性別:{}\t分類:{}\t".format(k,*v,space=chr(12288)))

while 1:
    choice = input("請輸入選項(1)列出目前神奇寶貝資料(2)依據身高排列(3)依據體重排列(4)找分類(5)找特性(6)找性別(7)離開：")
    if choice =='1':
        [pokemonformat(k,v) for (k, v) in pokemon.items()]
    elif choice =='2':
        [pokemonformat(k,v) for (k, v) in sorted(pokemon.items(), key=lambda x: x[1][1], reverse=True)]
    elif choice =='3':
        [pokemonformat(k,v) for (k, v) in sorted(pokemon.items(), key=lambda x: x[1][2], reverse=True)]
    elif choice =='4':
        attr = set()
        for k,v in pokemon.items():
            attr.add(v[5]) 
        print("目前分類列表為："+", ".join(str(e) for e in attr ))
        attrcho = input("請選擇要查詢的分類")
        [pokemonformat(k,v) for (k, v) in pokemon.items() if v[5]==attrcho]
    elif choice =='5':
        attr = set()
        for k,v in pokemon.items():
            attr.add(v[3]) 
        print("目前特性有：："+", ".join(str(e) for e in attr ))
        attrcho = input("請選擇要查詢的特性：")
        [pokemonformat(k,v) for (k, v) in pokemon.items() if v[3]==attrcho]
    elif choice =='6':
        attr = set()
        for k,v in pokemon.items():
            attr.add(v[4]) 
        print("目前性別有："+", ".join(str(e) for e in attr ))
        attrcho = input("請選擇要查詢的性別：")
        [pokemonformat(k,v) for (k, v) in pokemon.items() if v[4]==attrcho]
    elif choice =='7':
        break
        
