# reversing the string

a=("1,4,2,4")

def reversed_string():
    r=''
    for char in a:
       r=char+r
    return r
print(reversed_string())