my_list= [10, 20, 30, 40]
my_list.insert(1, 15)
print(my_list)  # Output: [10, 15, 20, 30, 40]

my_list.extend([50, 60, 70])
print(my_list)  # Output: [10, 15, 20, 30, 40, 50, 60, 70]

my_list.remove(70)
print(my_list)  # Output: [10, 15, 20, 30, 40, 50, 60]

my_list.sort(reverse=False)
print(my_list)  # Output: [10, 15, 20, 30, 40, 50, 60]

my_list.index(30)
print(my_list)  # Output: 3

my_list.index(30, 2, 5)
print(my_list)  # Output: 3