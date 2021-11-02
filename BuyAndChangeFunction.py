name = str (input("Good day! Please enter your nickname: "))
# this will greet the person's name
def greet(name):
    print ("Good day "+ str(name), "! Please enjoy your shopping.")
greet(name)

def getMoney():
    money = input("How much money do you have on hand?: ")
    return money

def askForApplePrice():
    priceOfApple = input("What is the current cost of an apple?: ")
    return  priceOfApple

money = getMoney()
priceOfApple = askForApplePrice()