# find two number from the list which adds up to the given target 

# A=[1,4,7,3,8,5]
# target=7


# def calc():
#     for i in range (len(A)):
#         for j in range(i+1,len(A)):
#            if A[i] + A[j]==target:
#               print('numbers are',A[i],A[j])
# calc()
  



# holding the first and last value of a list

# a=[7,3,9,1,4,2]
# target=(1,6)

# def calc():

#    first_value=(a[0])
#    sum=-1
#    b=len(a)
#    s=sum+b
#    last_value=(a[s])
#    print(f'{first_value},{last_value}')
# calc()
   



import math

n=1221

if n > 0:
    digits = int(math.log10(n))+1
    print(digits)
elif n == 0:
    digits = 1
    print(digits)
else:
    digits = int(math.log10(-n))+2 # +1 if you don't count the '-' 
    print(digits)






   
   
   