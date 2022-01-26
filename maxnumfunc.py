
def maxnumfunc(num1: int,num2: int,num3: int) -> int:
    maxnum = 0
    if(num1 > num2):
        maxnum = num1
    else:
        maxnum = num2
    if(maxnum < num3):
        maxnum = num3
    return maxnum

print(str(maxnumfunc(10, 40, 15)))   


def maxnumfunc(list1: list) -> int:
    maxnum = 0
    for x in list1:
        if(x > maxnum):
            maxnum = x
    
    return maxnum

mylist = [1,2,3,1,40,50,70,1,2,4,5,6,7]

print("Maximum number in the provided list is: " + str(maxnumfunc(mylist)))