print("\t\t\t\t\t\t\t\t\t\t..######...######...######...######...######...#.....#...######...######..\n\t\t\t\t\t\t\t\t\t\t....##.....#....#...#........#....#...#........#.....#...#....#...#.......\n\t\t\t\t\t\t\t\t\t\t....##.....#.##.....######...######...######...#.....#...#.##.....######..\n\t\t\t\t\t\t\t\t\t\t....##.....#...#....#........#....#........#...#.....#...#...#....#.......\n\t\t\t\t\t\t\t\t\t\t....##.....#....#...######...#....#...######...#######...#....#...######..")
input("Welcome to the Game 🎯\nPress Enter to start the Game.")
print("You are stuck in a two-way road and the treasure️️🏴‍☠️ lies at the end of one road.")
print("(R): Choose Right Road.")
print("(L): Choose Left Road.")
choice1=input("Enter your choice: ")
if (choice1 == "R"):
  print("(A): Carry a heavy box on your back and your distance will reduce to half.")
  print("(B): Wear skates and your distance will be doubled.")
  print("(C): Take any motor vehicle and your distance will become three times the original distance.")
  choice2=input("Enter your choice: ")
  if (choice2 == "A"):
    print("You have reached the end of the road but find no treasure\nWhat will you do?")
    print("(A): Break the box.")
    print("(B): Leave the box and go home.")
    choice3=input("Enter your choice: ")
    if (choice3 == "A"):
      print("Congrats! You found the Treasure 🏆.")
    elif (choice3 == "B"):
      print("Game Over!")
    else:
        print("Invalid Choice. Please restart the game by reloding the page.")
  elif (choice2 == "B"):
    print("You have reached the end of the road but find no treasure\nWhat will you do?")
    print("(A): You will keep those skates.")
    print("(B): You will sell those skates.")
    choice4=input("Enter your choice: ")
    if (choice4 == "A"):
      print("Congrats! You found the Treasure 🏆.")
    elif (choice4 == "B"):
      print("Game Over!")
    else:
      print("Invalid Choice. Please restart the game by reloding the page.")
  elif (choice2 == "C"):
    print("You have reached the end of the road but find no treasure\nWhat will you do?")
    print("(A): You will leave the car behind.")
    print("(B): You will sell the car.")
    choice5=input("Enter your choice: ")
    if (choice5 == "B"):
      print("Congrats! You found the Treasure 🏆.")
    elif (choice5 == "A"):
      print("Game Over!")
    else:
      print("Invalid Choice. Please restart the game by reloding the page.")
  else:
      print("Invalid Choice. Please restart the game by reloding the page.")
elif(choice1 == "L"):
  print("(A): Reload the game and choice the right road")
  print("(B): Press this and take the treasure")
  choice6=input("Enter your choice: ")
  if (choice6 == "A"):
    print("Congrats! You found the Treasure 🏆.")
  elif (choice6 == "B"):
    print("Game Over! You Lost! ❌")
  else:
    print("Invalid Choice. Please restart the game by reloding the page.")
else:
  print("Invalid Choice. Please restart the game by reloding the page.")
