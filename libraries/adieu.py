import inflect

names = []
while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        print()
        break

p = inflect.engine()
print(f"Adieu, adieu, to {p.join(names)}")
