# Linear Search Algorithm

arr = [7,9,35,67,22,4567,3456,568778787,22234,]
x = 3456
N = len(arr)

for i in range(0, N):
    if (arr[i] == x):
      print(i)
else:
    print(f'integer "{x}" does not exist in the array')