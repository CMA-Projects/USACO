"""
You are given a sorted array of N integers and a target integer. 
Your task is to determine whether the target integer is present in the array using Binary Search. 
If the target is found, output the index of the target (0-based). If the target is not found, output -1.


The input file file.in contains:
    1. The first line contains the integer N (1 ≤ N ≤ 100,000), the number of integers in the array.
    2. The second line contains N sorted integers.
    3. The third line contains the target integer to search for.

    
The output file file.out should contain:
    1. The index of the target integer if it is present in the array, or -1 if the target integer is not present.
"""

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Read input from file.in
with open("file.in", "r") as file:
    n = int(file.readline().strip())
    array = list(map(int, file.readline().strip().split()))
    target = int(file.readline().strip())

# Perform binary search
result = binary_search(array, target)

# Write output to file.out
with open("file.out", "w") as file:
    file.write(str(result) + "\n")

