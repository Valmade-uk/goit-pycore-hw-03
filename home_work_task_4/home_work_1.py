from datetime import datetime

def get_days_from_today(date:str):
    try:
        # Перетворення рядка у дату
        users_date = datetime.strptime(date, "%Y-%m-%d").date()
        # Отримання поточної дати
        current_date = datetime.now().date()
        # Різниця у днях
        days_since = (current_date - users_date).days
        return days_since
    except ValueError as e:
        print(f"Invalid date format: {e}")

print(get_days_from_today("2024-06-10"))