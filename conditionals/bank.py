def greeting(value):
    value = value.strip().lower()
    if value.startswith("hello"):
        return 0
    if value.startswith("h"):
        return 20
    return 100


if __name__ == "__main__":
    print(f"${greeting(input('Greeting: '))}")
