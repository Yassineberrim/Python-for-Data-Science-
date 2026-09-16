import sys


def main():
    """Check if the given number is odd or even."""
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) == 1:
            return
        assert sys.argv[1].lstrip('-').isdigit(), "argument is not an integer"
        number = int(sys.argv[1])
        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()