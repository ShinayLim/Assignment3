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

costOfApple = askForNumberOfApple()
costOfOrange = askForNumberOfOrange()