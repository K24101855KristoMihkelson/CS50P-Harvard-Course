def is_valid(s):
    if len(s) < 2 or len(s) > 6 or not s[:2].isalpha() or not s.isalnum():
        return False

    for i, char in enumerate(s):
        if char.isdigit():
            return char != "0" and s[i:].isdigit()
    return True


if __name__ == "__main__":
    print("Valid" if is_valid(input("Plate: ")) else "Invalid")
