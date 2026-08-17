from datetime import date

import inflect

p = inflect.engine()


def minutes_since(birth_date):
    today = date.today()
    delta = today - birth_date
    return int(delta.total_seconds() // 60)


def main():
    birth = input("Date of Birth: ")
    year, month, day = map(int, birth.split("-"))
    minutes = minutes_since(date(year, month, day))
    print(p.number_to_words(minutes, andword="").capitalize() + " minutes")


if __name__ == "__main__":
    main()
