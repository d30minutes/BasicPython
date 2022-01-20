

def myfirstfunction(*param2) -> str:
    print(str(len(param2)) + " This is the first liine of the function")
    print(type(param2))
   
    return "Hello"


myfirstfunction("a","b","c")


def names(firstname, lastname):
    print(lastname + " " + firstname)



names(lastname="Walter", firstname="Jamie")
names("Walter", "Jamie")


def kargsnames(**args):
   for x in args.keys():
       print(args[x])


kargsnames(lastname="Walter", firstname="Jamie", middlename=" K. ")

def nonmandatorparams(param1="default value"):
    print(" non mandatory params " + param1)


nonmandatorparams()