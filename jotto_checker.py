def HasDupes(word_to_dupe_check):  # checks for dupes
    letters = list(word_to_dupe_check)  # all letters
    no_rep = set(letters)  # unique letters
    if len(letters) > len(
        no_rep
    ):  # returns true if there are more letters than unique letters
        return True
    else:
        return False


def main():
    # initialize variables
    valid_secret = False  # will track if secret has five chars
    game_over = False  # flag to indicate exit from loop
    secret_word = ""
    guess = ""
    score = 0
    color_start = "\033[92m"  # start printing in color
    color_end = "\033[0m"  # return to default text color

    while not valid_secret:  # collect secret word until we get a valid one
        if len(secret_word) == 5 and not HasDupes(secret_word):
            valid_secret = True
            secret_word_list = list(secret_word)
        else:
            if len(secret_word) != 5 and len(secret_word) != 0:
                print("The secret word must have five characters.")
            if HasDupes(secret_word):
                print("The secret word must not have repeating letters.")

            print("\n")
            secret_word = input("What is your word? ").upper()
    print(
        "------------------------------------------------------"
    )  # divides secret collection from guess collection
    print("\nThe secret word is " + color_start + secret_word + color_end + ".\n")
    while not game_over:
        if guess == secret_word:
            print(color_start + "They got it!" + color_end)
            game_over = True
        elif len(guess) == 5 and not HasDupes(guess):
            guess_list = list(guess)
            # compare guess to secret word and count here
            for i in secret_word_list:
                for j in guess_list:
                    if i == j:
                        score = score + 1
            print(
                color_start
                + guess
                + color_end
                + ": "
                + color_start
                + str(score)
                + color_end
                + "\n"
            )
            score = 0  # reset variables for next iteration
            guess = ""  # reset variables for next iteration
        else:
            if len(guess) != 5 and len(guess) != 0:
                print("The guess must have five characters.")
            if HasDupes(guess):
                print("The guess must not have repeating letters.")
            guess = input("What was their guess? ").upper()


if __name__ == "__main__":
    main()
