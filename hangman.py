# Write your code here
import random
game_state = "play"
word_list = ['python', 'java', 'kotlin', 'javascript']
print('H A N G M A N')
print("")
chosen_word = random.choice(word_list)
list_lines = list('-' * len(chosen_word))
list_chosen = list(chosen_word)
counter = 0
char_try = set()
def game():
    global counter
    while counter < 8:
        print("")
        join_word = "".join(list_lines)
        print(join_word)
        if join_word == chosen_word:
            break
        user_letter = input("Input a letter: ")
        if len(user_letter) != 1:
            print("You should input a single letter")
        elif not user_letter.islower():
            print("It is not an ASCII lowercase letter")
        elif user_letter in char_try:
            print("You already typed this letter")
        elif user_letter in list_chosen:
            char_try.add(user_letter)
            for i, char in enumerate(list_chosen):
                if char == user_letter:
                    list_lines[i] = char
        else:
            print("No such letter in the word")
            counter += 1
            char_try.add(user_letter)
    if list_lines != list_chosen:
        print("You are hanged!")
    else:
        print("""You guessed the word!
You survived!""")

while game_state != "exit":
    game_state = input('Type "play" to play the game, "exit" to quit:')
    if game_state == "play":
        game()