array = [1,2, 3 , 4,  9 ,10]
search = 10

start = 0
end = len(array) - 1

found = False

while start <= end:
    mid = int(start + (end-start) / 2)

    if array[mid] == search:
        found = True
        break
    elif array[mid] > search:
        end = mid
    else:
        start = mid + 1

print(found)

