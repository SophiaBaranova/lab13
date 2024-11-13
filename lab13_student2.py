import json
import csv

#Бєлік Максим КН-32.1
try:
    #Відкриття json файлу
    with open('data.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
except FileNotFoundError:
    print("Файл data.json не знайдено, буде використано порожній список.")
    data = []
except IOError as e:
    print("Помилка доступу до JSON файлу:", e)
    data = []

# Додаємо нові записи до даних
new_entries = [
    {"порода": "лабрадор", "ім'я": "Шарик", "вік (міс)": "4"},
    {"порода": "чіхуахуа", "ім'я": "Карамелька", "вік (міс)": "2"}
]
data.extend(new_entries)

try:
    # Відкриваємо CSV файл для запису
    with open('data.csv', 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ["порода", "ім'я", "вік (міс)"]  # Імена стовпців

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)


        try:
            writer.writeheader()  # Записуємо заголовки
            writer.writerows(data) # Записуємо всі рядки з даними
            print("Успішний запис інформації")
        except csv.Error as e:
            print("Помилка запису в CSV файл:", e)
except IOError as e:
    print("Помилка доступу до CSV файлу:", e)
