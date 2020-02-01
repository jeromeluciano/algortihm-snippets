def swap(arr):
    temp = arr[0]
    arr[0] = arr[1]
    arr[1] = temp
    return arr

a = [2,3]
print(swap(a))
print(a)
