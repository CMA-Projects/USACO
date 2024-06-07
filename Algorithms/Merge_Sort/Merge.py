# Merge sort implementation in Python

# First subarry is arr[left to mid]
# Second subarray is arr[mid+1 to right]
def merge(array, left, mid, right):
    subArrayOne = mid - left + 1
    subArrayTwo = right - mid

    # Create temporary array
    leftArray = [0] * subArrayOne
    rightArray = [0] * subArrayTwo

    # Copy the data onto the temp arrays
    for i in range(subArrayOne):
        leftArray[i] = array[left + i]
    for j in range(subArrayTwo):
        rightArray[j] = array[mid + 1 + j]

    # Initialize the pointers
    indexOfSubArrayOne = 0
    indexOfSubArrayTwo = 0
    indexOfMergedArray = left

    # Merge the temp arrays back into array[left...right]
    while indexOfSubArrayOne < subArrayOne and indexOfSubArrayTwo < subArrayTwo:
        if leftArray[indexOfSubArrayOne] <= rightArray[indexOfSubArrayTwo]:
            array[indexOfMergedArray] = leftArray[indexOfSubArrayOne]
            indexOfSubArrayOne += 1
        else:
            array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo]
            indexOfSubArrayTwo += 1
        indexOfMergedArray += 1
    
    # Copy the remaining elements of the left[], if any
    while indexOfSubArrayOne < subArrayOne:
        array[indexOfMergedArray] = leftArray[indexOfSubArrayOne]
        indexOfSubArrayOne += 1
        indexOfMergedArray += 1
    
    # Copy the remaining elements of the right[], if any
    while indexOfSubArrayTwo < indexOfSubArrayTwo:
        array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo]
        indexOfSubArrayTwo += 1
        indexOfMergedArray += 1

def mergeSort(array, begin, end):
    if begin >= end:
        return
    mid = begin + (end - begin) // 2
    mergeSort(array, begin, mid)
    mergeSort(array, mid + 1, end)
    merge(array, begin, mid, end)

def printArray(array, size):
    for i in range(size):
        print(array[i], end = " ")
    print()

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    arr_size = len(arr)

    print("Unsorted array: ")
    printArray(arr, arr_size)

    mergeSort(arr, 0, arr_size - 1)

    print("\nSorted array: ")
    printArray(arr, arr_size)
