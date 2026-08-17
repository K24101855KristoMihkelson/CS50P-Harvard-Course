import random


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in {1, 2, 3}:
                return level
        except ValueError:
            pass


def generate_integer(level):
    ranges = {1: (0, 9), 2: (10, 99), 3: (100, 999)}
    return random.randint(*ranges[level])


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        for attempt in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    score += 1
                    break
                print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(f"{x} + {y} = {x + y}")

    print(f"Score: {score}")


if __name__ == "__main__":
    main()
