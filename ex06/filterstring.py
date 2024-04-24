from ft_filter import ft_filter
import sys


def validate_input() -> None:
    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")
    try:
        int(sys.argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad")


def get_input_list() -> list[str]:
    return sys.argv[1].split()


def filterstring():
    min_length = int(sys.argv[2])
    output = ft_filter(
        lambda x=min_length: len(x) >= min_length, get_input_list()
    )
    print(output)


def main():
    try:
        validate_input()
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")
        sys.exit(1)

    filterstring()


if __name__ == "__main__":
    main()
