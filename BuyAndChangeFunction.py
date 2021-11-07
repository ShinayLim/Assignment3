#This will show the shop's name
def myprint(): 
   print("Welcome to Fruity Shop!")

# this will greet the person's name
def greet():
    name = str (input("Good day! Please enter your nickname: "))
    print ("Good day "+ str(name), "! Please enjoy your shopping.")

def askForMoneyYouHave():
    money = input("How much money do you have on hand?: ")
    money = int(money)
    return money

def askForPriceOfApple():
    priceOfApple = input("What is the current cost of an apple?: ")
    priceOfApple = int(priceOfApple)
    return priceOfApple

def numberOfApplesYouCanBuy():
    numOfApple = customersMoney//applePrice
    return numOfApple

def yourChange():
    change = customersMoney%applePrice
    return change

def displayOutput():
    print(f"You can buy {numOfApple} apples and your change is {change} pesos.")

myprint()
greet()
customersMoney = askForMoneyYouHave()
applePrice = askForPriceOfApple()
numOfApple = numberOfApplesYouCanBuy()
change = yourChange()
displayOutput()