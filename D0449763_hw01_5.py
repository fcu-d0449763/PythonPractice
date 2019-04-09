# HW5
string = input()
string = string.replace(' ', '').split(",")
a = int(string[0])
b = int(string[1])

def GCD(a, b):
    m = a % b
    while (m > 0):
            a = b
            b = m
            m = a % b
    return str(b)

def LCM(a, b):
    return str(a * b // int(GCD(a, b)))

print("gcd = "+GCD(a,b),end=";")
print("lcm = "+LCM(a,b))