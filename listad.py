def list_operations(initial_list):
    my_list = initial_list

    while True:
        print("\nCurrent List:", my_list)
        print("1. Append an element")
        print("2. Extend with another list")
        print("3. Remove an element")
        print("4. Reverse the list")
        print("5. Count occurrences of an element")
        print("6. Find index of an element")
        print("7. Find minimum element")
        print("8. Find maximum element")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            element = input("Enter the element to append: ")
            my_list.append(element)
            print("Element appended successfully!")

        elif choice == '2':
            other_list = input("Enter the elements to extend (separated by space): ").split()
            my_list.extend(other_list)
            print("List extended successfully!")

        elif choice == '3':
            element = input("Enter the element to remove: ")
            if element in my_list:
                my_list.remove(element)
                print("Element removed successfully!")
            else:
                print("Element not found in the list.")

        elif choice == '4':
            my_list.reverse()
            print("List reversed successfully!")

        elif choice == '5':
            element = input("Enter the element to count occurrences: ")
            count = my_list.count(element)
            print(f"'{element}' appears {count} times in the list.")

        elif choice == '6':
            element = input("Enter the element to find its index: ")
            if element in my_list:
                print(f"Index of '{element}':", my_list.index(element))
            else:
                print(f"'{element}' not found in the list")

        elif choice == '7':
           
                min_element = min(my_list)
                print(f"The minimum element in the list is: {min_element}")
        elif choice == '8':
            
                max_element = max(my_list)
                print(f"The maximum element in the list is: {max_element}")
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-9).")

if __name__ == "__main__":
    initial_input = input("Enter the initial elements of the list (separated by space): ").split()
    list_operations(initial_input)
