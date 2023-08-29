"""
Exercise 2

Write a function that takes in two lists and returns the two lists merged together and sorted
Hint: You can use the .sort() method

add the lists together, and then sort them.
found the combine command.

"""

list_1 = [1,2,3,4,5,6]
list_2 = [3,4,5,6,7,8,10]
new_list=[]

def combine(list_1, list_2):
    new_list = sorted(list_1 + list_2)
    return new_list
 
final= combine(list_1, list_2)

print(final)