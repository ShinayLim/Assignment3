#This will show the shop's name
def myprint(): 
   print("Welcome to Fruity Shop!")
myprint()

name = str (input("Good day! Please enter your nickname: "))
# this will greet the person's name
def greet(name):
    print ("Good day "+ str(name), "! Please enjoy your shopping.")
greet(name)

#this will ask the customer the number of
#   apples and oranges they want to have
#   and its total cost

applePrice = 20
orangePrice = 25

def askForNumberOfApple():
    applesYouWantToBuy = input("How many apple/s you want to add in your cart?: ")
    costOfApple = int(applesYouWantToBuy) * applePrice
    return costOfApple

def askForNumberOfOrange():
    orangesYouWantToBuy = input("How many orange/s you want to add in your cart?: ")
    costOfOrange = int(orangesYouWantToBuy) * orangePrice
    return costOfOrange

def totalAmountOfApplesOranges():
    totalAmount = costOfApple + costOfOrange
    return totalAmount

def totalPurchase():
    print(f"The total amount is {totalAmount}")

costOfApple = askForNumberOfApple()
costOfOrange = askForNumberOfOrange()
totalAmount = totalAmountOfApplesOranges()
totalPurchase()

# this will ask the person if he or she will continue the purchase
def askYesNoQuestion(question):
  YesNoAnswer = input(question).upper()
  if YesNoAnswer == "YES" or YesNoAnswer == "NO":
     return YesNoAnswer  
  else:
     return askYesNoQuestion(question)
 
answer = askYesNoQuestion("Do you want to continue your transaction? (Yes or No) ")
if answer == "YES":
    print("The parcel is on your way. Thank you and come again!")
elif answer == "NO":
    print("Thank you for your time please come again!")

