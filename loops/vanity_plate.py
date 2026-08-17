def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False
    if not s[:2].isalpha():
        return False

    found_digit = False
    for ch in s:
        if ch.isdigit():
            if not found_digit and ch == "0":
                return False
            found_digit = True
        elif found_digit:
            return False
        elif not ch.isalpha():
            return False
    return True


plate = input("Plate: ")
print("Valid" if is_valid(plate) else "Invalid")
