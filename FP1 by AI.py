import random
import time

# Have a greeting that asks the user for their name.
user_name = input("Hello! What is your name? ")

# Greet the user by their name.
print(f"Hello, {user_name}! Let's generate some lucky PowerBall numbers for you.")
print("-" * 50)

# Generate the six random numbers for the powerball.
# The first five numbers are between 1 and 69.
white_ball_1 = random.randint(1, 69)
white_ball_2 = random.randint(1, 69)
white_ball_3 = random.randint(1, 69)
white_ball_4 = random.randint(1, 69)
white_ball_5 = random.randint(1, 69)

# The sixth number (PowerBall) is between 1 and 26.
red_ball = random.randint(1, 26)

# Print the numbers with a delay for dramatic effect.
print("Your lucky numbers are:")
print(f"White balls: {white_ball_1}", end="")
time.sleep(1)
print(f"  {white_ball_2}", end="")
time.sleep(1)
print(f"  {white_ball_3}", end="")
time.sleep(1)
print(f"  {white_ball_4}", end="")
time.sleep(1)
print(f"  {white_ball_5}")
time.sleep(1.5)
print(f"PowerBall:   {red_ball}")

print("-" * 50)

# Farewell message.
print("Good luck with your PowerBall ticket! I hope these are your winning numbers.")
print(f"Have a great day, {user_name}!")
