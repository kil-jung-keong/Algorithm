## 버블정렬
array1 = [9,8,7,6,5,4,3,2,1]
def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
print("before: ",array1)
bubble_sort(array1)
print('after: ',array1)

## 선택 정렬
array2 = [8,4,6,2,9,1,3,7,5]
def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
        print(array[:i+1])

print("before: ",array2)
selection_sort(array2)
print("after: ",array2)

## 병합 정렬
array3 = [8,4,6,2,9,1,3,7,5]
def merge_sort(array):
    if len(array) < 2:
        return array
    mid = len(array) // 2
    low_arr = merge_sort(array[:mid])
    high_arr = merge_sort(array[mid:])
    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1

    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    print(merged_arr)
    return merged_arr
print('before: ',array3)
array = merge_sort(array3)
print("after: ",array)

## 퀵정렬
array4 = [8,4,6,2,5,1,3,7,9]
def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = len(array) // 2
    front_arr, pivot_arr, back_arr = [], [], []
    for value in array:
        if value < array[pivot]:
            front_arr.append(value)
        elif value > array[pivot]:
            back_arr.append(value)
        else:
            pivot_arr.append(value)
    print(front_arr, pivot_arr, back_arr)
    return quick_sort(front_arr) + quick_sort(pivot_arr) + quick_sort(back_arr)
    