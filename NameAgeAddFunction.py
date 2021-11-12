def greet():
  name = str (input("Welcome to our shop, what is your nickname? "))
  print("Hello, "+name+". Good Morning!")

import sys
def askYesNoQuestion():
    answer = input("Are we allowed to gather personal information from you? ").upper()
    if answer == "YES":
        print("We highly appreciate that. We may now proceed. ")
    elif answer == "NO":
        print("We understand your privacy concerns.Thank you.")
        sys.exit()
    return answer
        
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

greet()
askYesNoQuestion()
name = getName()
age = getAge()
address = getAddress()
displayOutput(name, age, address)