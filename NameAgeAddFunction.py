name = str (input("Welcome to our shop, what is your nickname? "))
# this will greet the person's name
def greet(name):
    print("Hello, "+name+". Good Morning!")
greet(name)

# this will ask the person if the system is allowed to have their personal details
def askYesNoQuestion(question):
  YesNoAnswer = input(question).upper()
  if YesNoAnswer == "YES" or YesNoAnswer == "NO":
     return YesNoAnswer  
  else:
     return askYesNoQuestion(question)

import sys

answer = askYesNoQuestion("Are we allowed to gather personal information from you? (Yes or No) ")
if answer == "YES":
  print("We highly appreciate that. We may now proceed.")
elif answer == "NO":
    print("We understand your privacy concerns.Thank you.")
    sys.exit()
    
#gathering of the personal details...
def getName():
    nameFunc = input("Enter your full name: ")
    return nameFunc

def getAge():
    ageFunc = input("How old are you? ")
    return ageFunc

def getAddress():
    addFunc = input("Where do you live? ")
    return addFunc

def displayOutput(nameF, ageF, addF):
  print ("Please check if your information below is right...")
  print (f"Hi, my name is {nameF}. I am {ageF} years old and I live in {addF}.")

name = getName()

age = getAge()

address = getAddress()

displayOutput(name, age, address)