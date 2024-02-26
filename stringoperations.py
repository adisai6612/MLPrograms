# Initializing an empty list
my_list = []

while True:
    print("\nCurrent List:", my_list)
    print("1. Append an element")
    print("2. Extend the list")
    print("3. Remove an element")
    print("4. Reverse the list")
    print("5. list1")
    print("7. min")
    print("8. count")
    print("9.Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        element = input("Enter the element to append: ")
        my_list.append(element)

    elif choice == '2':
        elements = input("Enter elements to extend (comma-separated): ").split(',')
        my_list.extend(elements)
        
    elif choice == '3':
        element = input("Enter the element to remove: ")
        if element in my_list:
            my_list.remove(element)
        else:
            print("Element not found in the list.")
    elif choice == '4':
        my_list.reverse()
        print("List reversed.")
    elif choice =='5':
         print("Current List:", my_list)
    elif choice =='6':
        print("Maximum value:", max(my_list))
    elif choice =='7':
        print("Minimum value:", min(my_list))
    elif choice =='8':
        print(f"Count of {my_list}':", my_list.count(my_list))
    elif choice =='9':
        print("Minimum value:", min(my_list))
    elif choice == '10':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")