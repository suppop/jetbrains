# Write your code here
import random
options = ["rock", "paper", "scissors"]
user_choice = ""
comp_choice = ""
name = input("Enter your name: ")
print(f"Hello, {name}")
game_list = input()
print("Okay, let's start")
if len(game_list) > 0:
    options = game_list.split(",")
corent_score = 0
file = open('rating.txt', 'r')
for line in file:
    x = line.split()
    if x[0] == name:
        corent_score = int(x[1])
        break
file.close()
while True:
    user_choice = input()
    comp_choice = random.choice(options)
    if user_choice == "!exit":
        print("Bye!")
        break
    if user_choice == "!rating":
        print(f"Your rating: {corent_score}")
        continue
    if user_choice not in options:
        print("Invalid input")
        continue
    comp_idx = options.index(comp_choice)
    user_idx = options.index(user_choice)
    if user_idx > comp_idx:
        user_idx -= len(options)
    if user_choice == comp_choice:
        print(f"There is a draw ({comp_choice})")
        corent_score += 50
    elif comp_idx - user_idx <= len(options) // 2:
        print(f"Sorry, but computer chose {comp_choice}")
    else:
        print(f"Well done. Computer chose {comp_choice} and failed")
        corent_score += 100