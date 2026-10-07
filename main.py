import random
secret_number=random.radint(1,10)
print("Welcom to the guessing Game!!")
guess=int(input("Guessa number between 1 to 10:"))
if guess==secret_number:
  print("Awesome! You guessed it right!!")
else:
  print(f"Oops! The correct number was {secret_number}.")
