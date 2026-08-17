while True:
    try:
        x, y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)
        if y == 0:
            raise ZeroDivisionError
        percent = round(x / y * 100)
        if percent <= 1:
            print("E")
        elif percent >= 99:
            print("F")
        elif percent <= 100:
            print(f"{percent}%")
        else:
            continue
        break
    except (ValueError, ZeroDivisionError):
        pass
