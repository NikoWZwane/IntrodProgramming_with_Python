months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
date = input("Date: ").strip()
try:
    if "/" in date:
        month, day, year = date.split("/")
        month = int(month)
        day = int(day)
        year = int(year)
    else:
        month_str, day_year = date.split(" ", 1)
        day, year = day_year.replace(",","").split(" ")
        month = months.index(month_str)
        day = int(day)
        year = int(year)
    print(f"{year:04}-{month:02}-{day:02}")

except Exception:
    print("invalid date")

