arr = [1,2, 54,3,9,4, 9]

for i in range (len(arr)):
    for j in range (i+1, len(arr)):
        if(arr[i] > arr[j]):
            arr[i], arr[j] = arr[j], arr[i]

print(arr)