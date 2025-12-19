#Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.

Sample_List = ['abc', 'xyz', 'aba', '1221']
count=0
for number in Sample_List:
    count=count+1
print("The no.of strings in Sample_list is:",count)
count_1=0
for number in Sample_List:
    if (len(number) >= 2) and number[0] == number[-1]:
        count_1=count_1+1
print(count_1)
