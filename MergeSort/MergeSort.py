import sys

sorted_arr = []


def merge_sort(arr):
    global sorted_arr

    if len(arr) == 0:
        return

    left_arr = []
    right_arr = []

    for i in range(len(arr)):
        if i <= (0 + len(arr) - 1) // 2:
            left_arr.append(arr[i])
        else:
            right_arr.append(arr[i])

    if len(arr) > 1:
        merge_sort(left_arr)
        merge_sort(right_arr)
    else:
        sorted_arr = merge_arr(arr, sorted_arr)
    print(sorted_arr)


# merging two sorted arrays to a new sorted array
def merge_arr(arr1, arr2):
    new_arr = []
    i = 0
    j = 0
    for k in range(len(arr1) + len(arr2)):
        if i >= len(arr1) and j < len(arr2):
            new_arr.append(arr2[j])
            j += 1
            continue

        if j >= len(arr2) and i < len(arr1):
            new_arr.append(arr1[i])
            i += 1
            continue

        if arr1[i] <= arr2[j]:
            new_arr.append(arr1[i])
            i += 1
        else:
            new_arr.append(arr2[j])
            j += 1
    return new_arr


if __name__ == '__main__':
    arr = [5, 2, 4, 3, 7, 6, 8, 1, 9, 0]
    merge_sort(arr)