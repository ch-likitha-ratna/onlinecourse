import re
hand=open('example.txt')
x=list()
sum=0
for line in hand:
    y=re.findall('[0-9]+',line)
    x=x+y
for s in x:
    sum=sum+int(s)
print(sum)