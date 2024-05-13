# Develop a program that accept an input string, count occurrences of all characters within a string

input_str=input("enter the string\n")

set1=set(input_str)

for el in set1:
    count=0
    for char in input_str:
        if el==char:
            count+=1
    print("count of character '{}' is {}".format(el,count))