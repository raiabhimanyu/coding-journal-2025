#for i in range(1,6,2):
# print(i)
#else:
# print("bs")

#range is range(1,5)-->1 2 3 4
#range is range(1,5,2)-->1 3 

#if u break else in doesnt happen and else is optional
Y=False
while Y==True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    print('Length of the string is', len(s))
else:
    print('Done')




for i in range(1, 5):
    print (i)
else:
    print ('The for loop is over')



while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        print ('Input is of sufficient length')
        continue
    