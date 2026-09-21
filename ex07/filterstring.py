import sys


def main():
    try:
        assert len(sys.argv) == 3, "bad argument"
        S = sys.argv[1]
        N = int(sys.argv[2])
        words = S.split()


        islong = lambda word :len(word) > N
        result = [word for word in words if islong(word)]



        print(result)

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()