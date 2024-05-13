str_input=input("enter the list of element seperated by space\n")

li=[int(el)for el in str_input.split()]

for el in li:
    if((el*el)%8==0):
        print(el,end=" ")