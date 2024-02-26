# Take user input as a string
user_input = input("Enter a string of characters: ")

# Convert the user input string to a list of characters
char_list = list(user_input)

# Slicing: Extract a portion of the list
start_index = int(input("Enter the start index for slicing: "))
end_index = int(input("Enter the end index (exclusive) for slicing: "))
sliced_list = char_list[start_index:end_index]

# Counting: Count the occurrences of a specific character
char_to_count = input("Enter a character to count: ")
count = char_list.count(char_to_count)

# Indexing: Find the index of a specific character
char_to_find = input("Enter a character to find its index: ")
if char_to_find in char_list:
    index = char_list.index(char_to_find)
else:
    index = -1  # Character not found

# Sorting: Sort the list of characters
sorted_list = sorted(char_list)

# Print the results
print("Original List:", char_list)
print("Sliced List:", sliced_list)
print(f"Count of {char_to_count}:", count)
print(f"Index of {char_to_find}:", index if index != -1 else "Character not found")
print("Sorted List:", sorted_list)

