# hangman game in python
# it enables the randomzing thingy
import random
import time
from typing import Counter

#here we initialize the program
print("\nWelcome to hangman!")
#words_to_guess=input("\nEnter the words to be guessed:") 
player = input("\nWhat's your name, player:")
print("\nHello,",player.capitalize(),"Best of luck :-)")
time.sleep(1)
print("\nthe game is about to begin!\nlet's play hangman!!")
time.sleep(1)

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    word_to_guess= []
    word_to_guess=[item for item in input("Enter the words to be guessed: ").split()]
    word = random.choice(word_to_guess)
    length = len(word)
    count = 0
    display = "_"*length
    already_guessed = []
    play_game = ""

# A loop to re-execute the game when the first round ends:

def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()




def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    
    limit = 9
    guess = input ("This is the hangman word "+ display + "\nEnter your guess: ")
    guess = guess.strip()
    if len(guess.strip())== 0 or len(guess.strip())>=2 or guess <= "9":
        print("Invalid input, try a letter")
        hangman()
    
    # checks the 
    elif guess in word:
        # like append but cuter of course
        already_guessed.extend([guess])
        # find that in that
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        #display that after that
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |     | \n"
                  "  |        \n"
                  "__|__\n")
            print("Wrong guess." + str(limit - count) + " guesses remaining\n")
        elif count == 6:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /| \n"
                  "  |        \n"
                  "__|__\n")
            print("Wrong guess." + str(limit - count) + " guesses remaining\n")

        elif count == 7:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |         \n"
                  "__|__\n")
            print("Wrong guess." + str(limit - count) + " guesses remaining\n")

        elif count == 8:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    /  \n"
                  "__|__\n")
            print("Wrong guess." + str(limit - count) + " last guess remaining\n")

        elif count == 9:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",already_guessed,word)
            play_loop()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()


main()
hangman()


# the limit of tries, let's go with 7 because i am an amazing human being.
# the words to be guesssed, here let's have the overseer write them down,
# then we'll have the computer/program choose a random word from the ones given by the overseer
# after the random thingy, the player is asked to identify themselves so it looks like it cares about the player
# they are then given the number of words the word has.
# they then begin the game
