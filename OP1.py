
user_input = input("Enter a list of numbers separated by spaces: ")
user_input_list = [int(x) for x in user_input.split()]


start = int(input("Enter the start index for slicing: "))
end = int(input("Enter the end index (exclusive) for slicing: "))
sliced_list = user_input_list[start:end]

element_to_count = int(input("Enter an element to count: "))
count = user_input_list.count(element_to_count)


element_to_find = int(input("Enter an element to find its index: "))
if element_to_find in user_input_list:
    index = user_input_list.index(element_to_find)
else:
    index = -1  


sorted_list = sorted(user_input_list)

print("Original List:", user_input_list)
print("Sliced List:", sliced_list)
print(f"Count of {element_to_count}:", count)
if index != -1:
    print(f"Index of {element_to_find}:", index)
else:
    print(f"{element_to_find} not found in the list.")
print("Sorted List:", sorted_list)
