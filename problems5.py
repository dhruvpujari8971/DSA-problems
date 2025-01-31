# holding largest element in the array

arr=[3,1,32,99,123,66,183]

n=len(arr)
a=arr[0]

for i in range(1,n):
    if arr[i]>a:
        a=arr[i]
print(a)

