import random
answer = random.randint(1, 100)
max_attempts = 5
print("Guess the number!!")
print("The random number is generated automatically, Try to guess it! ")
for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Attempt {attempt} of {max_attempts}: Enter your guess: "))
    if guess < answer:
        print("Too low!")
    elif guess > answer:
        print("Too high!")
    else:
        print("Correct number!")
        break
else:
    print("Game Over! The correct number was", answer)
