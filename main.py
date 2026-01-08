from lexer import tokenize
from parser import check_syntax
from corrector import auto_correct

def main():
    with open('samples/input.java', 'r') as f:
        code = f.read()

    print("Original Code:\n")
    print(code)

    tokens = tokenize(code)
    errors = check_syntax(tokens)

    print("\nDetected Syntax Issues:")
    if errors:
        for e in errors:
            print("-", e)
    else:
        print("No syntax errors detected.")

    corrected_code = auto_correct(code)

    with open('samples/corrected.java', 'w') as f:
        f.write(corrected_code)

    print("\nCorrected Code Generated.")

if __name__ == "__main__":
    main()
