#Write a Python script to sort (ascending and descending) a dictionary by value.
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
def sort_asc(x):
    return sorted(x,key=value)
def value(n):
    return d[n]
def sort_desc(x):
    sorted(x,key=value,reverse=True)

sort_asc(d)
sort_desc(d)