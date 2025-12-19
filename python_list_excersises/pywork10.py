#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
Sample_List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#del Sample_List[0]
#del Sample_List[4]
#del Sample_List[5]
#if using del del from higher indices first
List=[item for (n,item) in enumerate(Sample_List) if n not in [0,4,5]]

print(List)
#would love to learn a bit more list comprehension

nums = [1, 2, 3, 4, 5]
# Output: [1, 4, 9, 16, 25]
Sq = [x**2 for x in nums]

names = ['alice', 'bob', 'charlie']
# Output: ['ALICE', 'BOB', 'CHARLIE']
NAMES = [x.capitalize for x in names]

nums = [5, 10, 15]
# Output: [15, 20, 25]
addten = [x+10 for x in nums]

nums = [1, 2, 3, 4, 5, 6]
# Output: [2, 4, 6]
even = [x for x in nums if x%2==0]

words = ['hi', 'hello', 'yes', 'python', 'ok']
# Output: ['hello', 'python']
threelong=[x for x in words if len(x)>3]

nums = [-3, -1, 0, 2, 4]
# Output: [0, 2, 4]
wholenum=[x for x in nums if x>=0]

colors = ['Red', 'Green', 'White', 'Black', 'Pink']
# Output: ['Red', 'White', 'Pink']
newlist=[x for (n,x) in enumerate(colors) if n%2==0]

nums = [10, 20, 30, 40, 50]
# Output: [10, 30, 50]
remlist=[x for (n,x) in nums if n in (0,2,4)]

nums = [1, 2, 3]
# Output: ['1', '2', '3']
stringlist=[str(x) for x in nums]

nums = [3, -2, 5, -1]
# Output: [3, 0, 5, 0]
zeropadder=[x for x in nums if x/x==-1 x=0]

