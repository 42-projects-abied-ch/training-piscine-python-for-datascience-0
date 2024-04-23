import sys


def validate_input() -> int:
    if (argc := len(sys.argv)) != 2:
        raise AssertionError(f"'whatis.py' takes exactly one (1) command line argument (got {argc})")
    try:
        argument = int(sys.argv[1])
    except ValueError:
        raise AssertionError(f"'whatis.py' takes only an integer as an argument; got '{sys.argv[1]}' ({type(sys.argv[1]).__name__})")
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