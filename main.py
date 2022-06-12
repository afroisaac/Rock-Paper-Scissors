import random
characters = {"R" : "Rock", "P": "Paper", "S": "Scissors"}
winnerFound = False

print("Game is starting...........")

while(winnerFound == False):
    firstPlayer = input("Pick from this options [R, P, S]:")
    if(firstPlayer.upper() not in characters):
        print("Error, input not in options listed")
        continue

    cpu = random.choice(list(characters))

    print("Player (", characters[firstPlayer], ") : CPU (", characters[cpu], ")" )

    if((firstPlayer.upper() == "R") and (cpu == "S")):
        print("Player wins") 
        winnerFound = True
    elif((cpu == "R") and firstPlayer.upper() == "S" ):
        print("CPU wins")
        winnerFound = True
    elif((firstPlayer.upper() == "P") and cpu == "R" ):
        print("Player wins")
        winnerFound = True
    elif((cpu == "P") and firstPlayer.upper() == "R" ):
        print("CPU wins")
        winnerFound = True
    elif((firstPlayer.upper() == "S") and cpu == "P" ):
        print("Player wins")
        winnerFound = True
    elif((cpu == "S") and firstPlayer.upper() == "P" ):
        print("CPU wins")
        winnerFound = True
    elif(firstPlayer.upper() == cpu):
        winnerFound = False
        continue
