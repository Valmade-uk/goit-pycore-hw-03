import re

def normalize_phone(phone_number):
    # Удаляем все лишние символы, кроме цифр и +
    phone_number = re.sub(r'[^\d+]', '', phone_number.strip())

    # Если номер начинается с +380 — оставляем как есть
    if phone_number.startswith('+380'):
        return phone_number

    # Если начинается с 380 — добавляем +
    if phone_number.startswith('380'):
        return '+' + phone_number

    # Иначе просто добавляем +38 перед цифрами
    digits = re.sub(r'\D', '', phone_number)
    return '+38' + digits

# Пример использования:
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

# Нормализуем все номера
sanitized = [normalize_phone(num) for num in raw_numbers]

# Выводим результат
print("Нормализованные номера:", sanitized)