import random

# %%
answer = random.randint(1, 101)
counter = 0

while True:
    counter += 1
    guess = input("What's your guess: \n")
    try:
        if int(guess) == answer:
            print(f"Bingo!\nYou've taken {counter} times to guess.")
            
            break
        elif int(guess) < answer:
            print("Bigger!\n")
        elif int(guess) > 100:
            print("Too Big! Smaller than 100.\n")
        else:
            print("Smaller!\n")
    except:
        print('input not valid, wasted a chance\n')


# %%
