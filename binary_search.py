def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = [1,6,7,8,0,99,101,27,8]
arr.sort() ## Array should be sorted.
target = 101
print(binary_search(arr,target))