
shoplist = ['apple', 'mango', 'carrot', 'banana']#This is a list

print ('I have', len(shoplist), 'items to purchase.') #len(list) gives length

for item in shoplist: #iterates through the list and prints each one of em
    print (item)

shoplist.append('rice')  #adds one more element at the end of the list
print ('My shopping list is now', shoplist)


shoplist.sort() #sorts in alphabetical order
print('Sorted shopping list is', shoplist)

print ('The first item I will buy is', shoplist[0]) #prints 1st item
olditem = shoplist[0] #variable is set
del shoplist[0] #the 1st item in list is deleted
print ('I bought the', olditem)
print ('My shopping list is now', shoplist)

shoplist[3]=watermelon