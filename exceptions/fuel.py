while True:
    try:
        x, y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)
        if y == 0:
            continue
        pct = round((x / y) * 100)
        if pct <= 1:
            print("E")
        elif pct >= 99:
            print("F")
        else:
            print(f"{pct}%")
        break
    except (ValueError, ZeroDivisionError):
        pass
