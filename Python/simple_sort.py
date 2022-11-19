import random
import time

# Creating an unsorted array
n = int(input("Enter the number of elements: "))
random.seed(123)
ar = [random.randrange(0, 100) for i in range(n)]

# Printing the unsorted array
print(f"The unsorted array: {ar}")

# Log the start time stamp
start = time.time()

# Implementing the simple sorting algorithm
for i in range(n):
    for j in range(i+1, n):
        if ar[j] < ar[i]:
            temp = ar[i]
            ar[i] = ar[j]
            ar[j] = temp

# Log the end time stamp
end = time.time()

# Calculating time of run in 'ms'
t = (end - start) * 10**3

# Printing the sorted array
print(f"\nThe sorted array is: {ar}")

# Display the run time
print(f"Run time: {t:.06f}ms")