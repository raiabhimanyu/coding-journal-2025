zoo = ('wolf', 'elephant', 'penguin')#the tuple which is like list except immutable
print ('Number of animals in the zoo is', len(zoo)) #lenth
new_zoo = ('monkey', 'dolphin', zoo) #zoo is an element not 3 elements
print ('Number of animals in the new zoo is', len(new_zoo)) 
print ('All animals in new zoo are', new_zoo)
print ('Animals brought from old zoo are', new_zoo[2])# 2nd element 0 1 2
print ('Last animal brought from old zoo is', new_zoo[2][2])# 2nd element of the 2nd element 0 1 2
singleton = (2 , )#single tuple needs a ,
empty = ()
print(singleton);print(empty)