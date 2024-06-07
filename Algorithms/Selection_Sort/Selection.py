def selection_sort(arr):
    # Traverse through all the elements in the array
    for i in range (len(arr) - 1):
        # Find the minimum in unsorted array
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[minimum] > arr[j]:
                minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i]

def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], end = " ")

if __name__ == "__main__":
    array = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted array: ")
    print_array(array)

    print("Sorted Array")
    selection_sort(array)
    print_array(array)

