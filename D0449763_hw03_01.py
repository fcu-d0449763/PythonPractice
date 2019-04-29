#HW03_01

def price(dictobj):
    ticketPrice = {"星光票":150,"優待票":175,"團體票":230,"學生票":250,"全票":350,"二日票":450,"三日票":650,"全期間票":2500}
    num = 0
    for k,v in dictobj.items():
        if k in ticketPrice:
             num += v * ticketPrice[k]
                
    return num
ticket = { "星光票":2,"二日票":3 }
p = price(ticket)
print(p)