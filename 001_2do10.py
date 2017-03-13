"""
24.10.2016 16:06
2do10
Rejurhf
"""

x = str(input("Podaj liczbe w systemie dwojkowym: "))
w = 0

for i in range(0, len(x)):
    w *= 2
    if(x[i] == '1'):
        w += 1
        
print(w)