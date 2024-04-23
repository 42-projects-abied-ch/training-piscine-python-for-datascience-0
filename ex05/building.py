import sys
import string


def validate_argument() -> str:
    """Validate the command line argument
    Prompt the user for input if no argument is provided"""

    if (n := len(sys.argv)) > 2:
        raise AssertionError(
            "'building.py' takes max. one (1) command line argument"
        )
    elif n == 1:
        text = input("Enter a string: ")
    else:
        text = sys.argv[1]
    return text


def print_result(
    text_length: int,
    upper_count: int,
    lower_count: int,
    punctuation_count: int,
    digit_count: int,
    space_count: int,
):
    """Print the result of the text analysis"""

    print(f"The text contains {text_length} characters:")
    print(f"- {upper_count} upper letters")
    print(f"- {lower_count} lower letters")
    print(f"- {punctuation_count} punctuation marks")
    print(f"- {digit_count} digits")
    print(f"- {space_count} spaces")


def parse(text: str):
    """Parse the text and count the number of upper and
    lower case letters, punctuation marks, digits and spaces"""

    upper_count = 0
    lower_count = 0
    punctuation_count = 0
    digit_count = 0
    space_count = 0

    for char in text:
        upper_count += 1 if char.isupper() is True else 0
        lower_count += 1 if char.islower() is True else 0
        punctuation_count += 1 if char in string.punctuation else 0
        digit_count += 1 if char.isdigit() is True else 0
        space_count += 1 if char.isspace() is True else 0

    print_result(
        len(text),
        upper_count,
        lower_count,
        punctuation_count,
        digit_count,
        space_count,
    )


def main():
    try:
        text = validate_argument()
        parse(text)
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
