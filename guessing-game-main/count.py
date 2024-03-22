import random
print("Number guessing game")
number = random.randint(1, 9)
chances = 0
print("Guess a number (between 1 and 9:")

while chances <5:

      guess = int(input("Enter your guess:-  "))

      if guess == number:
            print("you won")
            break

      elif guess < number:
            print("you lost the number was", guess)

      else:
            print("your guess was too high the number was", guess)

      chances += 1

 if not chances <5:
      print("you lose the number was")