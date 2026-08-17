def value(greeting):
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):
        return 0
    if greeting.startswith("h"):
        return 20
    return 100
