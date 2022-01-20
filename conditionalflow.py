score = 40

if (score > 50 and score < 100):
    print("Score is still under 100")
elif (score >= 100):
    print("Big round of applause for the players to reach 100 runs mark!!!!")
else:
    print("Score is too low and below 50")



trafficlight = "BLANK"
isblinking = False

if trafficlight == "RED":
    print("Stop the vehicle before the white line.")
elif (trafficlight == "YELLOW" and isblinking == True):
    print("Watch the sides and ahead of the vehicle if the path is cleared and no hurdles around then start moving the vehicle!")
elif trafficlight == "YELLOW":
    print("Start the engine but do not move yet!!")
elif trafficlight == "GREEN":
    print("Start moving the vehicle forward.")
else:
    print("Wait for manual intervention to control the vehicle.")

