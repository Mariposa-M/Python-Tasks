# Create an empty list called my_list.
my_list = []
# Append the following elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

# Insert the value 15 at the second position in the list.
my_list.insert(1,15)
# Extend my_list with another list: [50, 60, 70].
list_extension = [50, 60, 70]
my_list.extend(list_extension)
print(my_list)
# Remove the last element from my_list.
print(my_list.pop())
# Sort my_list in ascending order.
my_list2 = my_list.sort()
# Find and print the index of the value 30 in my_list.
print(my_list.index(30))
