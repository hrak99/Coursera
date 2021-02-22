num1=list()
num=0
num=list()
import re
name='regex_sum_141075.txt'
inp=open(name)
for line in inp:
    y=re.findall('[0-9]+',line)
    num1=num1+y
#print (num1)
for line1 in num1:
    x=int(line1)
    num.append(x)
#print (x)
#print(num)
print (sum(num))
