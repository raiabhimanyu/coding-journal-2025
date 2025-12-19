#Write a Python program to remove duplicates from a list.
list=[1,2,3,2,4,5,6,7,8]
dupe_list=[]
for k in list:
    if k not in dupe_list:
        dupe_list.append(k)

print(dupe_list)
