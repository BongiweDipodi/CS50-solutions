import random
while True:
    try:
        level = int(input("Level: "))
        if level <= 0:
            raise ValueError
        break
    except ValueError:
        pass

x = list(range(1, level+1))
y = random.choice(x)

while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            raise ValueError
        if guess == y:
            print("Just right!")
            break
        elif guess > y:
            print("Too large!")
        else:
            print("Too small!")

    except ValueError:
        pass
