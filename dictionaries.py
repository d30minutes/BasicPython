list = ["Leather", "Black"]
mycar = {"brand":"Ford", "model":"Mustang", "year": 1965, "SeatCovers":list, "IsNew":True}


#print(mycar)

#print(mycar["brand"])

#print(len(mycar))

#print(mycar.get("SeatCovers"))

#print(mycar.get("NoOfSeats"))

#print(mycar.keys())

#for x in mycar.keys():
    #print(x, mycar[x])

#print(mycar.values())


mydict = {"Name": "Donald", "Country": "Australia", "Gender": "Male", "Age": 30, "IsAlive": True}
if "Name" in mydict:
  print("Yes, 'Name' is one of the keys in the mydict dictionary")


mydict["Name"] = "McDonalds"

#print(mydict)

mydict.update({"Country":"USA"})
print(mydict)

mydict.pop("Country")
print(mydict)

mydict.popitem()
print(mydict)

del mydict["Name"]
print(mydict)

del mydict
#print(mydict)

print("-----------------------")
#print(mycar)

#mycar.clear()

#print(mycar)

for x,y in mycar.items():
    print(x,y)

mustang = {"Model":"Mustang"}
toyota = {"Model":"Toyota"}
benz = {"Model":"Benz"}

cars = {"1":mustang, "2":toyota, "3": benz}
print(cars)



