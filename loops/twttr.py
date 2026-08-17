text = input("Input: ")
print("Output: ", end="")
for ch in text:
    if ch.lower() not in "aeiou":
        print(ch, end="")
print()
