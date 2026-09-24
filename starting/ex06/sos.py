"""Encode a given string into Morse code using sys.argv."""
import sys

MORSE_CODE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",
    " ": "/",
}


def main():
    """Encode the string given as argument into Morse code.

    Reads exactly one string argument from sys.argv, converts it to
    uppercase, then checks that every character has a Morse code
    equivalent. Prints the resulting Morse code, with each character's
    code separated by a single space. Raises an AssertionError if the
    number of arguments is wrong or if the string contains an
    unsupported character.
    """
    try:
        assert len(sys.argv) == 2, "the arguments are bad"

        text = sys.argv[1].upper()

        for c in text:
            if c not in MORSE_CODE:
                assert False, "the arguments are bad"

        codes = []
        for c in text:
            codes.append(MORSE_CODE[c])

        result = " ".join(codes)

        print(result)

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
