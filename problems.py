# find two number from the list which adds up to the given target 

A=[1,4,7,3,8,5]
target=7


def calc():
    for i in range (len(A)):
        for j in range(i+1,len(A)):
           if A[i] + A[j]==target:
              print('numbers are',A[i],A[j])
calc()
  










   
   
   