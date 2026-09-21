"""Filter words from a string based on their length."""
import sys


def main():
    """Filter words longer than N from a string given as arguments.

    Reads exactly two arguments from sys.argv: a string and an
    integer N. Prints the list of words from the string whose length
    is strictly greater than N. Raises an AssertionError if the
    number of arguments is wrong or if the types are incorrect.
    """
    try:
        assert len(sys.argv) == 3, "the arguments are bad"

        S = sys.argv[1]
        N_str = sys.argv[2]

        assert N_str.lstrip('-').isdigit(), "the arguments are bad"
        N = int(N_str)

        words = S.split()

        islong = lambda word: len(word) > N
        result = [word for word in words if islong(word)]

        print(result)

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()