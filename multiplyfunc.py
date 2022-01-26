def multplyfunc(list1):
    multipliedVal = 1
    for x in list1:
        multipliedVal *= x

    return multipliedVal


mylist = [1,2,3,4,5]

print("The total value of a list:" + str(mylist) + " is:" + str(multplyfunc(mylist)))