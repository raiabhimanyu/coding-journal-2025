#Write a Python script to check whether a given key already exists in a dictionary.
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
key = 7
print("Key exists" if key in d else "Key doesnt exist")