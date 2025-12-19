#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
Sample_List = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Define a function called 'last' that takes a single argument 'n' and returns the last element of 'n'

def sorted_list(x):
    return sorted(x,key=last)
def last(n):
    print(n)
    return n[-1]
sorted_list(Sample_List)