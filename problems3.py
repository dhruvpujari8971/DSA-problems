# reversing the integer value

s=1299391392392394934934934
a=0

while s!=0:
    b=s%10
    a=a*10+b
    s=s//10
print(a)

# counting the digits in interger

a=123456789876
r=0

while a!=0:
    b=a%10
    a=a//10
    r+=1

print(r)