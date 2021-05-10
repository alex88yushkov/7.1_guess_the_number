import random

rand = random.randrange(50)
print(rand)
print("Guess the number from 0 to 49")


def guess():
    num = int(input())
    if num == rand:
        print("You guessed correctly!")
        quit()
    elif num > rand:
        print("The value is too high")
    else:
        print("The value is too low")


count = 7
for attempt in range(7):
    count -= 1
    guess()
    print("You have", count, "attempts")
