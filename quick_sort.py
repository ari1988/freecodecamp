def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[-1]

    less_than_pivot = [x for x in array if x < pivot]
    equal_to_pivot = [x for x in array if x == pivot]
    greater_than_pivot = [x for x in array if x > pivot]

    return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot)