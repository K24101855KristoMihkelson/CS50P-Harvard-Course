months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date = input("Date: ").strip()
    try:
        if "/" in date:
            m, d, y = date.split("/")
            m, d, y = int(m), int(d), int(y)
        else:
            m_str, d, y = date.replace(",", "").split()
            m, d, y = months.index(m_str) + 1, int(d), int(y)

        if 1 <= m <= 12 and 1 <= d <= 31:
            print(f"{y:04d}-{m:02d}-{d:02d}")
            break
    except (ValueError, IndexError):
        pass
