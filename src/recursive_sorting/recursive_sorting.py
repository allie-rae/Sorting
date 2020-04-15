# TO-DO: complete the helper function below to merge 2 sorted arrays
import math



def merge( arrA, arrB ):
    left_index = 0
    right_index = 0
    new_arr = []
    while left_index < len(arrA) and right_index < len(arrB):
        if arrA[left_index] <= arrB[right_index]:
            new_arr.append(arrA[left_index])
            left_index = left_index + 1
        else: 
            new_arr.append(arrB[right_index])
            right_index = right_index + 1
    while left_index < len(arrA):
        new_arr.append(arrA[left_index])
        left_index = left_index + 1
    while right_index < len(arrB):
        new_arr.append(arrB[right_index])
        right_index = right_index + 1
    return new_arr



# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) < 2:
        return arr
    middle = int(math.floor(len(arr)/2))
    left = arr[0:middle]
    right = arr[middle:len(arr)]
    return merge(merge_sort(left), merge_sort(right))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
