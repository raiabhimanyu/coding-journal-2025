#Write a Python program to print the numbers of a specified list after removing even numbers from it.
list=[0,1,2,3,4,5,6]
even_list=[0]
even_list=[2*x for x in list]
sorted_list=[x for x in list if x in even_list]
print(sorted_list)


# Create a list 'num' containing several integer values
num = [7, 8, 120, 25, 44, 20, 27]

# Use a list comprehension to create a new list 'num' that includes only the elements from the original list
# where the element is not divisible by 2 (i.e., not even)
num = [x for x in num if x % 2 != 0]

# Print the modified 'num' list, which contains only odd values
print(num)
