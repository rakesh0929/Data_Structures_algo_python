def Linearsearch(arr,target):
    for i in arr:
        if (arr[i] == target):
            return f"The index of {target} is {i}"


l = Linearsearch([1,2,3,4,5],3)
print(l)