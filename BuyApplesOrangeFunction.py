def myprint(): 
   print("Welcome to Fruity Shop!")

def greet():
    name = str (input("Good day! Please enter your nickname: "))
    print ("Good day "+ str(name), "! Please enjoy your shopping.")


def askForNumberOfApple():
    applePrice = 20
    applesYouWantToBuy = input("How many apple/s you want to add in your cart?: ")
    costOfApple = int(applesYouWantToBuy) * applePrice
    return costOfApple

def askForNumberOfOrange():
    orangePrice = 25
    orangesYouWantToBuy = input("How many orange/s you want to add in your cart?: ")
    costOfOrange = int(orangesYouWantToBuy) * orangePrice
    return costOfOrange

def totalAmountOfApplesOranges():
    totalAmount = costOfApple + costOfOrange
    return totalAmount

def totalPurchase():
    print(f"The total amount is {totalAmount}")

def askYesNoQuestion():
    answer = input("Do you want to continue your transaction? ").upper()
    if answer == "YES":
        print("The parcel is on your way. Thank you and come again! ")
    elif answer == "NO":
        print("Thank you for your time please come again!")
    return answer

myprint()
greet()
costOfApple = askForNumberOfApple()
costOfOrange = askForNumberOfOrange()
totalAmount = totalAmountOfApplesOranges()
totalPurchase()
askYesNoQuestion()