from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()  # сьогоднішня дата
    result = []

    for user in users:
        # Перетворення рядка в дату
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        # День народження цього року
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо вже пройшов — дивимось наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Скільки днів до дня народження
        days_left = (birthday_this_year - today).days

        # Якщо день народження в межах 7 днів
        if 0 <= days_left <= 7:
            date_to_congratulate = birthday_this_year

            # Якщо це субота або неділя — переносимо на понеділок
            if date_to_congratulate.weekday() == 5:  # субота
                date_to_congratulate += timedelta(days=2)
            elif date_to_congratulate.weekday() == 6:  # неділя
                date_to_congratulate += timedelta(days=1)

            # Додаємо результат
            result.append({
                "name": user["name"],
                "congratulation_date": date_to_congratulate.strftime("%Y.%m.%d")
            })

    return result

# Приклад використання
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Alice Brown", "birthday": "1992.01.28"},
    {"name": "Bob Martin", "birthday": "1988.01.21"},
]

upcoming = get_upcoming_birthdays(users)

print("Кого вітати цього тижня:")
for user in upcoming:
    print(f"{user['name']} — {user['congratulation_date']}")