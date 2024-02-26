def list_operations(input_string):
    # Convert the input string to a list
    input_list = input_string.split()

    # Print the generated list
    print("Generated List:", input_list)

    # Minimum value in the list
    print("Minimum value:", min(input_list))

    # Maximum value in the list
    print("Maximum value:", max(input_list))

    # Count occurrences of a specific value in the list
    value_to_count = input("Enter a value to count: ")
    print(f"Count of '{value_to_count}':", input_list.count(value_to_count))

    # Index of a specific value in the list
    value_to_find = input("Enter a value to find its index: ")
    if value_to_find in input_list:
        print(f"Index of '{value_to_find}':", input_list.index(value_to_find))
    else:
        print(f"'{value_to_find}' not found in the list")

    element = input("Enter the element to append: ")
    input_list.append(element)
    print("Element appended successfully!")
# Take input as a string from the user
user_input = input("Enter elements separated by space: ")

# Perform list operations
list_operations(user_input)
