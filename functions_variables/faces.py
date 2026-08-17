def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")


def main():
    text = input("Input: ")
    print(convert(text))


if __name__ == "__main__":
    main()
