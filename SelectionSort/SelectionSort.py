def selection_sort(arr):
    if len(arr) == 0:
        return
    for i in range(len(arr)):
        i_min = i # n
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i_min]:
                i_min = j
        if i_min != i :
            temp = arr[i]
            arr[i] = arr[i_min]
            arr[i_min] = temp

# O(n2)

if __name__ == '__main__':
    arr = [5, 2, 4, 6, 9, 1, 7]
    selection_sort(arr)
    print(arr)