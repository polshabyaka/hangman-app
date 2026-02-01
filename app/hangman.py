def reveal_word(secret: str, guessed: set[str]) -> str:
    # Example: secret="python", guessed={"p"} -> "p _ _ _ _ _"
    return " ".join([ch if ch.lower() in guessed else "_" for ch in secret])


def is_word_guessed(secret: str, guessed: set[str]) -> bool:
    return all(ch.lower() in guessed for ch in secret)


def main() -> None:
    secret = "python"
    guessed: set[str] = set()
    wrong = 0
    max_wrong = 6

    print("Hangman")
    while wrong < max_wrong and not is_word_guessed(secret, guessed):
        print("\nWord:", reveal_word(secret, guessed))
        print(f"Wrong guesses: {wrong}/{max_wrong}")

        letter = input("Guess a letter: ").strip().lower()
        if len(letter) != 1 or not letter.isalpha():
            print("Enter one letter (a-z).")
            continue
        if letter in guessed:
            print("Already guessed.")
            continue

        guessed.add(letter)
        if letter in secret:
            print("Good guess!")
        else:
            wrong += 1
            print("Wrong guess!")

    if is_word_guessed(secret, guessed):
        print("\nYou won! Word was:", secret)
    else:
        print("\nYou lost! Word was:", secret)


if __name__ == "__main__":
    main()
