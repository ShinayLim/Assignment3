name = str (input("Welcome to our shop, what is your nickname? "))

def greet(name):
    print("Hello, "+name+". Good Morning!")
greet(name)

def askYesNoQuestion(question):
  YesNoAnswer = input(question).upper()
  if YesNoAnswer == "YES" or YesNoAnswer == "NO":
     return YesNoAnswer  
  else:
     return askYesNoQuestion(question)
 
answer = askYesNoQuestion("Are we allowed to gather personal information from you? (Yes or No) ")
if answer == "YES":
  print("We highly appreciate that. We may now proceed")
elif answer == "NO":
    print("We understand your provacy concerns.Thank you.")

def getName():
    nameFunc = input("Enter your full name: ")
    return nameFunc

def getAge():
    ageFunc = input("How old are you? ")
    return ageFunc

def getAddress():
    addFunc = input("Where do you live? ")
    return addFunc

