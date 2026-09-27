import random


# ============================================================
#                    HANGMAN GAME
# ============================================================

class HangmanGame:

    # Five predefined words as required by CodeAlpha
    WORDS = [
        "PYTHON",
        "COMPUTER",
        "PROGRAM",
        "DEVELOPER",
        "CODING"
    ]

    MAX_WRONG_GUESSES = 6

    # Hangman drawings for each wrong guess
    HANGMAN = [
        """
          +---+
          |   |
              |
              |
              |
              |
        =========
        """,

        """
          +---+
          |   |
          O   |
              |
              |
              |
        =========
        """,

        """
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========
        """,

        """
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========
        """,

        """
          +---+
          |   |
          O   |
         /|\\  |
              |
              |
        =========
        """,

        """
          +---+
          |   |
          O   |
         /|\\  |
         /    |
              |
        =========
        """,

        """
          +---+
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        =========
        """
    ]

    def __init__(self):
        self.word = ""
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.score = 0

    # --------------------------------------------------------
    # Start a new game
    # --------------------------------------------------------

    def new_game(self):
        self.word = random.choice(self.WORDS)
        self.guessed_letters.clear()
        self.wrong_guesses = 0

    # --------------------------------------------------------
    # Display the hidden word
    # --------------------------------------------------------

    def get_display_word(self):
        result = []

        for letter in self.word:
            if letter in self.guessed_letters:
                result.append(letter)
            else:
                result.append("_")

        return " ".join(result)

    # --------------------------------------------------------
    # Check if the word is completely guessed
    # --------------------------------------------------------

    def has_won(self):
        for letter in self.word:
            if letter not in self.guessed_letters:
                return False

        return True

    # --------------------------------------------------------
    # Display current game information
    # --------------------------------------------------------

    def display_status(self):

        print("\n" + "=" * 55)

        print(self.HANGMAN[self.wrong_guesses])

        print("WORD       :", self.get_display_word())
        print(
            "MISTAKES   :",
            f"{self.wrong_guesses}/{self.MAX_WRONG_GUESSES}"
        )
        print(
            "LIVES LEFT :",
            self.MAX_WRONG_GUESSES - self.wrong_guesses
        )

        if self.guessed_letters:
            letters = " ".join(sorted(self.guessed_letters))
            print("GUESSED    :", letters)
        else:
            print("GUESSED    : None")

        print("=" * 55)

    # --------------------------------------------------------
    # Get a valid letter from the player
    # --------------------------------------------------------

    def get_guess(self):

        while True:

            guess = input(
                "\nEnter a letter (or type EXIT): "
            ).strip().upper()

            # Exit option
            if guess == "EXIT":
                return None

            # Only one alphabetic character is allowed
            if len(guess) != 1 or not guess.isalpha():
                print(
                    "⚠️ Please enter exactly ONE letter."
                )
                continue

            # Prevent duplicate guesses
            if guess in self.guessed_letters:
                print(
                    f"⚠️ You already guessed '{guess}'. "
                    "Try another letter."
                )
                continue

            return guess

    # --------------------------------------------------------
    # Process player's guess
    # --------------------------------------------------------

    def process_guess(self, guess):

        self.guessed_letters.add(guess)

        if guess in self.word:

            print(
                f"\n✅ Excellent! '{guess}' is in the word."
            )

            self.score += 10

        else:

            self.wrong_guesses += 1

            print(
                f"\n❌ Sorry! '{guess}' is not in the word."
            )

    # --------------------------------------------------------
    # Display final result
    # --------------------------------------------------------

    def show_result(self):

        print("\n" + "=" * 55)

        if self.has_won():

            bonus = (
                self.MAX_WRONG_GUESSES - self.wrong_guesses
            ) * 5

            self.score += bonus

            print("🎉 CONGRATULATIONS!")
            print("You successfully guessed the word!")
            print("WORD  :", self.word)
            print("SCORE :", self.score)

        else:

            print("💀 GAME OVER!")
            print("The correct word was:", self.word)
            print("SCORE :", self.score)

        print("=" * 55)

    # --------------------------------------------------------
    # Run one complete round
    # --------------------------------------------------------

    def play_round(self):

        self.new_game()

        print("\n🎮 NEW HANGMAN ROUND")

        while (
            self.wrong_guesses < self.MAX_WRONG_GUESSES
            and not self.has_won()
        ):

            self.display_status()

            guess = self.get_guess()

            # Player chose EXIT
            if guess is None:

                print("\n👋 Thanks for playing!")
                return False

            self.process_guess(guess)

        self.display_status()
        self.show_result()

        return True


# ============================================================
#                    USER INTERFACE
# ============================================================

def show_welcome():

    print("\n" + "=" * 55)
    print("              🎯 HANGMAN CHALLENGE")
    print("=" * 55)

    print("Guess the hidden word one letter at a time.")
    print("You have 6 incorrect guesses.")
    print("Type EXIT at any time to quit.")

    print("=" * 55)


# ============================================================
#                    MAIN PROGRAM
# ============================================================

def main():

    show_welcome()

    game = HangmanGame()

    while True:

        if not game.play_round():
            break

        while True:

            choice = input(
                "\n🔄 Play again? (Y/N): "
            ).strip().upper()

            if choice in ("Y", "N"):
                break

            print("⚠️ Please enter Y or N.")

        if choice == "N":
            break

    print("\n" + "=" * 55)
    print("🏆 THANK YOU FOR PLAYING HANGMAN!")
    print("FINAL SCORE:", game.score)
    print("=" * 55)


# ============================================================
#                    PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()