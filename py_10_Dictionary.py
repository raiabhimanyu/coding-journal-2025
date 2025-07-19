#!/usr/bin/python3
# Filename: using_dict.py

# 'ab' is short for 'address book'
ab = {
    'Swaroop': 'swaroopch@byteofpython.info',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's address is", ab['Swaroop'])

# Adding a key/value pair
ab['Guido'] = 'guido@python.org'

# Deleting a key/value pair
del ab['Spammer']

print(ab)

print(f"\nThere are {len(ab)} contacts in the address-book\n")

for name, address in ab.items():
    print(f'Contact {name} at {address}')

if 'Guido' in ab:
    print(f"\nGuido's address is {ab['Guido']}")


