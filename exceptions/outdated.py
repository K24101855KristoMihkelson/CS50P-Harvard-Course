months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date = input("Date: ").strip()
    try:
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
        else:
            month_name, day, year = date.split(" ")
            month = months.index(month_name) + 1
            day = int(day.replace(",", ""))
        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"{int(year):04d}-{month:02d}-{day:02d}")
            break
    except (ValueError, IndexError):
        pass
