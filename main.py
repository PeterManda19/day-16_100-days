import time

print("Welcome to the 'Name the Lyrics' game.")
print()
time.sleep(1)
print("I will write my favorite song lyrics with a word missing.")
print()
time.sleep(2)
print("""You are going to figure out the correct song lyric in as few attempts as possible.""")

print()
time.sleep(2)
print("Everytime you key in your response press enter. Goodluck!!!")

def showWinMessage(count):
  print("Well done! It only took you", count,"attempts.")  
  print() 

exit = ""
quitComList = ['y', 'yes','exit', 'quit']
while exit not in quitComList:
  print()
  print("Fill in the blank lyrics!")
  print()
  
  give = ""
  count = 0
  while give.lower() != "give":
    count+=1
    print()
    time.sleep(1)
    give = input("""Would you ____ me tonight.
""")
    
    if count == 2 and give.lower() != "give" :
      print("You lost! you have used all your", count,"attempts.")
      print("Fill in the next one.")
      break
    elif give.lower() != "give":
      print()
      print(2 - count, "attempts left.")
    elif give.lower() == "give":
      showWinMessage(count)
    
  rest = ""
  count = 0
  while  rest.lower() != "rest":
    count+=1
    print()
    time.sleep(1)
    rest = input("""And the ____ of your life?
""")
    if count == 2 and rest.lower() != "rest":
      print("You lost! you have used all your", count,"attempts.")
      print("Fill in the next one.")
      break
    elif rest.lower() != "rest":
      print()
      print(2 - count, "attempts left.")  
    elif rest.lower() == "rest":
      showWinMessage(count) 

  have = ""
  count = 0
  while  have.lower() != "have":
    count+=1
    print()
    time.sleep(1)
    have = input("""I wanna ____ it all with you."
""")
    if count == 2 and have.lower() != "have":
      print("You lost! you have used all your", count,"attempts.")
      print("Fill in the next one.")
      break
    elif have.lower() != "have":
      print()
      print(2 - count, "attempts left.")  
    elif have.lower() == "have":
      showWinMessage(count)


  biblical = ""
  count = 0
  while  biblical.lower() != "biblical":
    count+=1
    print()
    time.sleep(1)
    biblical = input("""Cause your love is ________.
""")
    if count == 2 and biblical.lower() != "biblical":
      print("You lost! you have used all your", count,"attempts.")
      print("Fill in the next one.")
      break
    elif biblical.lower() != "biblical":
      print()
      print(2 - count, "attempts left.") 
    elif biblical.lower() == "biblical": 
      showWinMessage(count)

  reason = ""
  count = 0
  while  reason.lower() != "reason":
    count+=1
    print()
    time.sleep(1)
    reason = input("""Cause I need you to see that you are the ______.
""")
    if count == 2 and reason.lower() != "reason":
      print("You lost! you have used all your", count,"attempts.")
      print("Fill in the next one.")
      break
    elif reason.lower() != "reason":
      print()
      print(2 - count, "attempts left.") 
    elif reason.lower() == "reason":  
      showWinMessage(count)
   
  decision = ""
  count = 0
  while  decision.lower() != "decision":
    count+=1
    print()
    time.sleep(1)
    decision = input("""Love is just a ________, the choice is yours.
""")
    if count == 2 and decision.lower() != "decision":
      print("You lost! you have used all your", count,"attempts.")
      print("Try again.")
      break
    elif decision.lower() != "decision":
      print()
      print(2 - count, "attempts left.")  
    elif decision.lower() == "decision": 
      showWinMessage(count)

  while True:
    exit = input("Would like to exit the game? ")
    y = ['y','yes']
    n = ['n', 'no']
    if exit.lower() in y:
      break
    elif exit.lower() in n:
      continue
    else:
      print("please answer 'yes' or 'no' ")
      print()
      print("You can also use 'y' for yes or 'n' for no")
      continue


def endGame():
  while True:
    print()
    input("""Thank you for playing!
To play again please click Stop on top right page and click Run """)
    print()
    continue


if __name__=="__main__":
  endGame()