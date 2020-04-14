# TO-DO: Complete the selection_sort() function below
#
# Algorithm
# Start with current index = 0

# For all indices EXCEPT the last index:

# a. Loop through elements on right-hand-side of current index and find the smallest element

# b. Swap the element at current index with the smallest element found in above loop
#
#


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        for each in range(i+1, len(arr)):
            if arr[each] < arr[smallest_index]:
                smallest_index = each
        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# Loop through your array
# Compare each element to its neighbor
# If elements in wrong position (relative to each other, swap them)
# If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.

# TO-DO:  implement the Bubble Sort function below

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]


def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        for current_index in range(len(arr)-1):
            if arr[current_index] > arr[current_index+1]:
                arr[current_index +
                    1], arr[current_index] = arr[current_index], arr[current_index+1]
                swapped = True
        if swapped == False:
            break
    return arr


print(bubble_sort(arr1))

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
