# Guess the word game
# One player inputs word for other person to guess and vice versa
# Need to make another function for each player's turn

def guess_word():
    word1 = input("Player one, input a word: ").upper()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    word2 = input("Player two, input a word: ").upper()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    game1 = False
    game2 = False
    arr1 = list(word1)
    arr2 = list(word2)
    guessed_letters1 = []
    guessed_letters2 = []
    guessed_words1 = []
    guessed_words2 = []
    word_completion1 = "_" * len(word2)
    word_completion2 = "_" * len(word1)

    while not game1 and not game2:
        # Player 1 turn
        print("-----PLAYER ONE-----")
        print(guessed_letters1, "\n")
        guess1 = input("Guess: ").upper()

        if len(guess1) == 1 and guess1.isalpha():
            if guess1 in guessed_letters1:
                print("You already guessed this letter.")
            elif guess1 not in word2:
                print(guess1, "is not in the word.")
                guessed_letters1.append(guess1)
            else:
                print(guess1, "is in the word!")
                guessed_letters1.append(guess1)
                word_as_list1 = list(word_completion1)
                indices = [i for i, letter in enumerate(word2) if letter == guess1]
                for index in indices:
                    word_as_list1[index] = guess1
                word_completion1 = "".join(word_as_list1)
                if "_" not in word_completion1:
                    game1 = True
        elif len(guess1) == len(word2) and guess1.isalpha():
            if guess1 in guessed_words1:
                print("You already guessed that word.")
            elif guess1 != word2:
                print(guess1, "is not the word.")
                guessed_words1.append(guess1)
            else:
                game1 = True
                word_completion = word2
        else:
            print("Not a valid guess.")
        print()
        print(word_completion1)
        print()

        # Check if player 1 won
        if game1 or game2:
            break

        # Player 2 Turn
        print("-----PLAYER TWO-----")
        print(guessed_letters2, "\n")
        guess2 = input("Guess: ").upper()

        if len(guess2) == 1 and guess2.isalpha():
            if guess2 in guessed_letters2:
                print("You already guessed this letter.")
            elif guess2 not in word1:
                print(guess2, "is not in the word.")
                guessed_letters2.append(guess2)
            else:
                print(guess2, "is in the word!")
                guessed_letters2.append(guess2)
                word_as_list2 = list(word_completion2)
                indices = [i for i, letter in enumerate(word1) if letter == guess2]
                for index in indices:
                    word_as_list2[index] = guess2
                word_completion2 = "".join(word_as_list2)
                if "_" not in word_completion2:
                    game2 = True
        elif len(guess2) == len(word1) and guess2.isalpha():
            if guess2 in guessed_words2:
                print("You already guessed that word.")
            elif guess2 != word1:
                print(guess2, "is not the word.")
                guessed_words2.append(guess2)
            else:
                game2 = True
                word_completion = word1
        else:
            print("Not a valid guess.")
        print()
        print(word_completion2)
        print()

    if game1:
        print("Congratulations Player One, you won!")
    elif game2:
        print("Congratulations Player Two, you won!")


guessWord()
