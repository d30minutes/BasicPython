

vehiclenumbers = ["LKR555", "WTP897", "TTR189", "LKF999", "ILOVEU", "I LOV S"]

#isfound = False
index = 0
vehicletofind = "I LOV S"

while(True):
    str1 = vehiclenumbers[index]
    index += 1
    print("Loop is running for index: " + str(index) + " and the vehicle number is: " + str1)

    if(str1 != vehicletofind):
        continue
    
    print("This statement is after continue")
    
    #if(str1 == vehicletofind):
    print("Vehicle is found in the index location:" + str(index))
    break
        #isfound = True

    