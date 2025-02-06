import random

#guess_count = 0


word_list = ["Stanley Park", "Queen Elizabeth Park", "Granville Island", "Gastown", "Kitsilano Beach",
              "English Bay", "Panorama Ridge", "Garibaldi Lake", "Deep Cove", "Lynn Canyon", "Victoria"]
#making a list with the words

print("Welcome to Hangman! Keep in mind some words have upper case words at the beginning")


#I used the previous lab for the list as reference made by hiro, this to give me an idea to make a base code with different functions
#and have them individually with def
#needed to define the wrong guesses option meaning the one it will be repeating the most

def show_wrong_guesses(wrong_guesses,guessed_letters):
    remaining_guesses = 6 - wrong_guesses
    #print("Welcome to Hangman! Keep in mind some words have upper case words at the beginning")
    print(f"Incorrect guesses remaining {remaining_guesses}")
    print("Guessed letters:", " ".join(guessed_letters))

def show_hint(hint):
    print(" ".join(hint))

def show_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(word_list)
    hint = ["_" if letter != " " else " "for letter in answer] #https://data-flair.training/blogs/python-operator/ I didn't knew how to say not
                                                                #equal to without using some loops
    wrong_guesses = 0
    guessed_letters = set()

    while True:
        show_wrong_guesses(wrong_guesses, guessed_letters)
        show_hint(hint)
        guess = input("Enter a letter:")

        if len(guess) >= 2 or not guess.isalpha():
            print("You are only able to guess one letter at the time")
            continue

        if guess in guessed_letters:
            print("This letter has already been guessed, keep in mind you will have to choose between upper and lowe case, depending on the letter")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
             if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            show_wrong_guesses(wrong_guesses, guessed_letters)
            print("You won :), the word was:", answer)
            break

        elif wrong_guesses >= 6:
            show_wrong_guesses(wrong_guesses, guessed_letters)
            print("Game over! The word was:", answer)
            break

if __name__ == "__main__":
    main()