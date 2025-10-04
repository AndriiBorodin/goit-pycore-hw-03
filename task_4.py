from datetime import datetime, date, timedelta

def get_upcoming_birthdays(users):
    today = date.today()
    result = []

    for i in users:
        bday = datetime.strptime(i["birthday"], "%Y.%m.%d").date()
        bday_this_year = date(today.year, bday.month, bday.day)


        if bday_this_year < today:
            continue


        if (bday_this_year - today).days <= 7:
            if bday_this_year.weekday() >= 5:
                bday_this_year += timedelta(days=7 - bday_this_year.weekday())

            result.append({
                "name": i["name"],
                "congratulation_date": bday_this_year.strftime("%Y.%m.%d")
            })

    return result

users = [
    {"name": "Гогі", "birthday": "1998.10.03"},
    {"name": "Олена", "birthday": "1998.10.04"},
    {"name": "Ігор",  "birthday": "1990.10.05"},
    {"name": "Іван",  "birthday": "1990.10.07"},
    {"name": "Марія",  "birthday": "1985.10.12"}
]

print(get_upcoming_birthdays(users))
