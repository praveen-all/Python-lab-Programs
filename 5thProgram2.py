# binary search 

def binarySearch(li,key):
    low=0
    high=len(li)-1
    while(low<=high):
        mid=(low+high)//2
        if(li[mid]==key):
           return mid 
        elif(li[mid]<key):
            low=mid+1
        else:
            high=mid-1
            
    return -1


str_input=input("enter the list seperated by space\n")
li=[int(el)for el in str_input.split()]
key=int(input("enter the key element to search\n"))

find=binarySearch(li,key)
if find==-1:
    print("{} element not found".format(key))
else:
    print("{} element found at a position {}".format(key,find))
        