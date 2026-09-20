"""Count upper, lower, punctuation, space and digit characters in a text."""
import sys
import string


def count_characters(text):
    """Count upper, lower, punctuation, space and digit characters.

    Takes a string and returns a tuple containing, in order, the number
    of uppercase letters, lowercase letters, punctuation marks, spaces
    and digits found in the string.
    """
    upper = 0
    lower = 0
    punct = 0
    space = 0
    digit = 0
    for c in text:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c.isdigit():
            digit += 1
        elif c.isspace():
            space += 1
        elif c in string.punctuation:
            punct += 1
    return upper, lower, punct, space, digit


def main():
    """Read a text from the arguments or user input and print counts.

    If exactly one argument is given, it is used as the text to analyze.
    If no argument is given, the user is prompted to enter a text.
    If more than one argument is given, an AssertionError is raised.
    """
    try:
        assert len(sys.argv) <= 2, "the arguments are bad"

        if len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            text = input("What is the text to count?\n")
        upper, lower, punct, space, digit = count_characters(text)
        print(f"The text contains {len(text)} characters:")
        print(f"{upper} upper letters")
        print(f"{lower} lower letters")
        print(f"{punct} punctuation marks")
        print(f"{space} spaces")
        print(f"{digit} digits")
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
