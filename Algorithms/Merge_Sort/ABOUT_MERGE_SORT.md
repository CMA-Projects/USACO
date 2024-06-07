# MERGE SORT ALGORITHM
Also follows the divide and conquer type of algorithm. It works recursively by dividing the array into smaller arrays and then sorting each sub array.

In simple terms, it divides the array into havles, sorts each half, and then merges back together

## Time Complexity
Best Case: O(n logn)

Average Case: O(nlogn)

Worst Case: O(nlogn)

The *Merge* portion of the algorithm takes O(n) to complete. This process is linear to the total number of elements n being merged.

However, the divide phase of the algorithm takes O(logn) time. It repatedly divides the array into halves recursively.