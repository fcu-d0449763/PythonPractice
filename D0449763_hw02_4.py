#HW02_5
import requests
import json
from pprint import pprint
headers = {
    'accept': 'application/json',
}

params = (
    ('Year', '105'),
    ('Month', '01'),
)

response = requests.get('http://datacenter.taichung.gov.tw/swagger/OpenData/fd55cb14-e526-4658-8a6b-045ab582a025', headers=headers, params=params)
res = json.loads(response.text)



dist ={}
vil = set()


for i in res:
    if i["區別"] not in dist:
        dist[i["區別"]]={"里別":[i["里別"]]}
        if i["性別"] == '計':
            dist[i["區別"]].update({"總計遷入":i["總計遷入"]})
            dist[i["區別"]].update({"總計遷出":i["總計遷出"]})
            dist[i["區別"]].update({"國內戶籍遷徙(含其他)_遷入":i["國內戶籍遷徙(含其他)_遷入"]})
            dist[i["區別"]].update({"國內戶籍遷徙(含其他)_遷出":i["國內戶籍遷徙(含其他)_遷出"]})
            dist[i["區別"]].update({"國際戶籍遷徙_遷入":i["國際戶籍遷徙_遷入"]})
            dist[i["區別"]].update({"國際戶籍遷徙_遷出":i["國際戶籍遷徙_遷出"]})
    elif i["里別"] not in  dist[i["區別"]]["里別"]:
        dist[i["區別"]]["里別"].append(i["里別"])
        if i["性別"] == '計':
            dist[i["區別"]]["總計遷入"] += i["總計遷入"]
            dist[i["區別"]]["總計遷出"] += i["總計遷出"]
            dist[i["區別"]]["國內戶籍遷徙(含其他)_遷入"] += i["國內戶籍遷徙(含其他)_遷入"]
            dist[i["區別"]]["國內戶籍遷徙(含其他)_遷出"] += i["國內戶籍遷徙(含其他)_遷出"]
            dist[i["區別"]]["國際戶籍遷徙_遷入"] += i["國際戶籍遷徙_遷入"]
            dist[i["區別"]]["國際戶籍遷徙_遷出"] += i["國際戶籍遷徙_遷出"]

print("分析總計遷入數前三區")
for x, v in sorted(dist.items(), key=lambda x: x[1]["總計遷入"], reverse=True)[:3]:
    print(x,"總計遷入:",v["總計遷入"])

print("\n分析總計遷出數前三區")
for x, v in sorted(dist.items(), key=lambda x: x[1]["總計遷出"], reverse=True)[:3]:
    print(x,"總計遷出:",v["總計遷出"])

print("\n分析國內戶籍遷徙(含其他)_遷入前三區")
for x, v in sorted(dist.items(), key=lambda x: x[1]["國內戶籍遷徙(含其他)_遷入"], reverse=True)[:3]:
    print(x,"國內戶籍遷徙(含其他)_遷入:",v["國內戶籍遷徙(含其他)_遷入"])
    
print("\n分析國內戶籍遷徙(含其他)_遷出前三區")
for x, v in sorted(dist.items(), key=lambda x: x[1]["國內戶籍遷徙(含其他)_遷出"], reverse=True)[:3]:
    print(x,"國內戶籍遷徙(含其他)_遷出",v["國內戶籍遷徙(含其他)_遷出"])
    
print("\n分析國際戶籍遷徙_遷入前三區")
for x, v in sorted(dist.items(), key=lambda x: x[1]["國際戶籍遷徙_遷入"], reverse=True)[:3]:
    print(x,"國際戶籍遷徙_遷入:",v["國際戶籍遷徙_遷入"])
    
print("\n分析國際戶籍遷徙_遷出前三區")
for x, v in sorted(dist.items(), key=lambda x: x[1]["國際戶籍遷徙_遷出"], reverse=True)[:3]:
    print(x,"國際戶籍遷徙_遷出:",v["國際戶籍遷徙_遷出"])
    
print("\n分析里數前三區")
for x, v in sorted(dist.items(), key=lambda x: len(x[1]["里別"]), reverse=True)[:3]:
    print(x,"里數:",len(v["里別"]))