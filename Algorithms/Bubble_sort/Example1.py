"""
You are given an array of N integers. Your task is to sort this array using Bubble Sort. 
Given an "file.in" file with the first line being the number N. The second line of "file.in" contains value of N integers.
Return the number of swaps needed to sort the array in the "file.out".
"""

# Read input from file.in
with open("file.in", "r") as file:
    # Read the first line
    N = int(file.readline().strip())

    # Read the second line
    line = file.readline()
    stripped_line = line.strip()
    str_list = stripped_line.split()
    int_list = map(int, str_list)
    array = list(int_list)

    # Read the second line (alternative)
    # array = list(map(int, file.readline().strip().split()))

#Bubble sort method that counts swaps
def bubble_sort(arr):
    n = len(arr)
    swap_count = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_count += 1
    return swap_count

# Perform bubble sort and count swaps
swap_count = bubble_sort(array)

# Write output to file.out
with open("file.out", "w") as file:
    file.write(str(swap_count) + "\n")

"""
The strip() method removes any leading and trailing whitespace characters (including newlines) from the string read by file.readline().
.split():

The split() method splits the stripped string into a list of substrings based on whitespace (by default, it splits by any whitespace and removes empty strings).
For example, if the line read is "5 3 2 4 1\n", after strip() and split(), it becomes ['5', '3', '2', '4', '1'].

map(int, ...):

The map() function applies the int function to each item in the list returned by split(). This converts each substring from a string to an integer.
Continuing from the previous example, map(int, ['5', '3', '2', '4', '1']) creates an iterator that produces [5, 3, 2, 4, 1].

list(...):

The list() function converts the iterator returned by map() into a list.
Therefore, list(map(int, ['5', '3', '2', '4', '1'])) results in the list [5, 3, 2, 4, 1].
    """