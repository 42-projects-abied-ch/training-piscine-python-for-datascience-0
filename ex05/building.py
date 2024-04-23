import sys

def validate_argument() -> bool:
    if len(sys.argv) > 2:
        raise AssertionError("'building.py' takes max. one (1) command line argument")
    

def main():
    try: 
        validate_argument()
    except AssertionError as e:
        print(f"{}")

if __name__ == "__main__":
    main()