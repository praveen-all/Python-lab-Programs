# merge sort
def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_half=arr[:mid]
    right_half=arr[mid:]
    
    left_half=mergeSort(left_half)
    right_half=mergeSort(right_half)
    return merge(left_half,right_half)
    
def merge(left,right):
    i=j=0
    result=[]
    while i<len(left) and j<len(right):
        if(left[i]<right[j]):
            result.append(left[i])
            i+=1
        else :
            result.append(right[j])
            j+=1
    
    result+=left[i:]
    result+=right[j:]
    return result
    
    
str_input=input("Enter the list of element seperated by space\n")
li=[int(el)for el in str_input.split()]
print("before sorting:",end="")
print(li,end="\n")
print("after sorting:",end="")
li=mergeSort(li)
print(li)
