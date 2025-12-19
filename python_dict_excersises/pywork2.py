#Write a Python script to add a key to a dictionary.

d = {0: 10, 1: 20}
#Expected Result = {0: 10, 1: 20, 2: 30}
d[2]=30
d.update({3:40})
print(d)