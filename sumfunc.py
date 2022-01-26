
def sumfunc(list1):
    totalval = 0
    for x in list1:
        totalval += x

    return totalval


mylist = [1,2,3,4,5]

#print(*mylist, sep = ", ")
#print(*mylist, sep = "\n")

print(''.join(str(mylist)))

#print("The total value of a list:" + str(mylist) + " is:" + str(sumfunc(mylist)))