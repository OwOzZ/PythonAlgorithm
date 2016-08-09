def insert_sort(arr):
    for j in range(1, len(arr)):
        curr = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > curr:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = curr


if __name__ == '__main__':
    array = [5, 2, 4, 9, 0, 7, 5]
    insert_sort(array)
    print(array)

