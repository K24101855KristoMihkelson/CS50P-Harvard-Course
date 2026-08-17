from datetime import date
import inflect


def minutes_since(birth_date):
    today = date.today()
    minutes = int((today - birth_date).total_seconds() // 60)
    p = inflect.engine()
    return f"{p.number_to_words(minutes, andword='').capitalize()} minutes"
