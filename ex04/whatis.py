import sys


def validate_input() -> int:
    if len(sys.argv) != 2:
        raise AssertionError("more than one argument is provided")
    try:
        argument = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")
    return argument


def whatis():
    argument = validate_input()
    print("I'm Even" if argument % 2 == 0 else "I'm Odd")


def main():
    try:
        whatis()
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
