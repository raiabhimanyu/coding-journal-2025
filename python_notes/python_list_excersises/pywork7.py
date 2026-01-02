#Write a Python program to clone or copy a list.
#list=[1,2,3,4]
#copy_list=[]
#for i in list:
    #copy_list.append(i)

#print(copy_list)

original_list = [10, 22, 44, 23, 4]

# Create a new list 'new_list' and copy the elements from 'original_list' into it
new_list = list(original_list)

# Print the contents of the 'original_list'
print(original_list)

# Print the contents of the 'new_list', which is a copy of 'original_list'
print(new_list)