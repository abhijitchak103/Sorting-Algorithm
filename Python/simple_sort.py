import random

# Creating an unsorted array
n = int(input("Enter the number of elements: "))

ar = [random.randrange(0, 100) for i in range(n)]

# Printing the unsorted array
print(f"The unsorted array: {ar}")

# Implementing the simple sorting algorithm
for i in range(n):
    for j in range(i+1, n):
        if ar[j] < ar[i]:
            temp = ar[i]
            ar[i] = ar[j]
            ar[j] = temp

# Printing the sorted array
print(f"\nThe sorted array is: {ar}")