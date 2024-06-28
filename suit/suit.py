import random

number = random.randint(1,10)
guess = input("Pilih angka dari 1 - 100 : ")
guess = int(guess)

print("Your Answer : ",guess)
print("Random Answer : ",number)

if guess == number:
    print("You Win!")
else:
    print("You Lose!")