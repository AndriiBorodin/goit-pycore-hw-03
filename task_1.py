from datetime import datetime


def get_days_from_today(date: str) -> int:
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = today - input_date
        return delta.days
    except ValueError:
        return ValueError("Невірний формат дати. Використовуйте формат 'РРРР-ММ-ДД'.")

print(get_days_from_today("2024-01-01"))
print(get_days_from_today("2026-01-01"))
print(get_days_from_today("test"))