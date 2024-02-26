# Perform different operations such as count slice index sort\


numbers = [5, 2, 8, 1, 9, 3, 6, 4, 7,10]

subset = numbers[2:6]  
print("Sliced subset:", subset)

count_of_3 = numbers.count(3)
print("Count of 3:", count_of_3)

index_of_9 = numbers.index(9)
print("Index of 9:", index_of_9)

numbers.sort()
print("Sorted list (ascending):", numbers)

#numbers.sort(reverse=True)
#print("Sorted list (descending):", numbers)

numbers.reverse()
print("reverse order:",numbers)
