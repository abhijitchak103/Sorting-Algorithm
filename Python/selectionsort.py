import random
import time

# Creating an unsorted array
n = int(input("Enter the number of elements: "))
random.seed(123)
ar = [random.randrange(0, 100) for _ in range(n)]

# Printing the unsorted array
print(f"The unsorted array: {ar}")

# Get the location of the next smallest element
def locofSmallest(ar: list, start: int):
    """
    Returns the index of the smallest element in an array in given range
    """
    j = ar.index(min(ar[start:]))

    return j

# Implementation of Selection Sort
def selSort(ar: list):
    """
    Implements the selection sort
    """
    i = 0                           # Initialize the pointer to 0
    n = len(ar)                     # Get the length of array to iterate over
    while i < n-1:                  # Iterate over the entire length of array. n-1 used as for n, i+1 will go out of index
        j = locofSmallest(ar, i)    # Find the index of next smallest element in the array
        swap(ar, i, j)              # Swaps the current element with next smallest element
        i += 1                      # Increment i by 1

# Swap the numbers, current number with next smallest (if any)
def swap(ar: list, x: int, y: int):
    """
    Swaps two values in an array
    """
    temp = ar[x]
    ar[x] = ar[y]
    ar[y] = temp

# Log the start time stamp
start = time.time()

# Call the Selection Sort function and run on the array
selSort(ar)

# Log the end time stamp
end = time.time()

# Calculating time of run in 'ms'
t = (end - start) * 10**3

# Display the sorted array
print(f"\nThe sorted array is: {ar}")

# Display the run time
print(f"Run time: {t:.06f}ms")