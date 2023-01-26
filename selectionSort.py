def selectionSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    for i in range(n):
        minm = arr[i]
        minmIndx = i
        for j in range(i, n):
            if arr[j] < arr[minmIndx]:
                minmIndx = j
                
        arr[i], arr[minmIndx] = arr[minmIndx], arr[i]
    
    return arr

arr = [8, 5, 7, 3, 2]
print(selectionSort(arr))