def bubbleSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    for i in range(n):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [8, 5, 7, 3, 2]
print(bubbleSort(arr))