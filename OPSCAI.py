# Create a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Slice the list to get a portion of it
sliced_numbers = numbers[2:6]  # This will slice elements from index 2 to 5 (inclusive)
print(sliced_numbers)  # Output: [3, 4, 5, 6]

# Count the occurrences of a specific element in a list
fruits = ["apple", "banana", "orange", "apple", "kiwi", "apple"]
count_apples = fruits.count("apple")
print("Count of apples:", count_apples)  # Output: Count of apples: 3

# Find the index of an element in a list
colors = ["red", "green", "blue", "yellow", "purple"]
index_blue = colors.index("blue")
print("Index of 'blue':", index_blue)  # Output: Index of 'blue': 2

# Sort a list in ascending order
numbers = [4, 1, 6, 3, 8, 2, 7, 5]
numbers.sort()
print("Sorted numbers:", numbers)  # Output: Sorted numbers: [1, 2, 3, 4, 5, 6, 7, 8]

# Sort a list in descending order
numbers.sort(reverse=True)
print("Reverse sorted numbers:", numbers)  # Output: Reverse sorted numbers: [8, 7, 6, 5, 4, 3, 2, 1]

# Create a sorted copy of a list without modifying the original
unsorted_numbers = [4, 1, 6, 3, 8, 2, 7, 5]
sorted_copy = sorted(unsorted_numbers)
print("Original list:", unsorted_numbers)
print("Sorted copy:", sorted_copy)
