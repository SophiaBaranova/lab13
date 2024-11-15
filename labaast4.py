import csv
import json

#Баранова Софія КН-31

#функція відкриття файлу
def openFile(file_name, mode):
    try:
        file = open(file_name, mode)
    except:
        print("файл", file_name, "не вдалося відкрити")
        return None
    else:
        return file

#дані для запису у csv файл
data = [
    {"порода": "пудель", "ім'я": "Бублик", "вік (міс)": 3},
    {"порода": "бігль", "ім'я": "Кексик", "вік (міс)": 1},
    {"порода": "мопс", "ім'я": "Пиріжок", "вік (міс)": 5}
]
#назви полів для csv файлу
fieldnames = ["порода", "ім'я", "вік (міс)"]

#створення csv файлу
csvfile = openFile("data.csv", "w")
if csvfile is not None:
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    #запис назв полів у csv файл
    writer.writeheader()
    #запис даних у csv файл
    writer.writerows(data)
    #закриття csv файлу
    csvfile.close()

#відкриття csv файлу
csvfile = openFile("data.csv", "r")
if csvfile is not None:
    reader = csv.DictReader(csvfile)
    #завантаження даних із csv файлу у list
    csv_data = list(reader)
    #перетворення list у рядок json
    json_data = json.dumps(csv_data, ensure_ascii = False, indent = 2)

    #створення json файлу
    jsonfile = openFile("data.json", "w")
    if jsonfile is not None:
        #запис даних у json файл
        jsonfile.write(json_data)
        #закриття json файлу
        jsonfile.close()

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


#Куцевол Аліса КН-32/1
#перетворення csv файлу на json
try:
    fieldnames = ["порода", "ім'я", "вік (міс)"]
    #відкриття файлу data.csv для додавання даних
    with open('data.csv', 'a', encoding='utf-8') as csvfile:
        #запис у файл нових даних
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writerow({"порода": "ротвейлер", "ім'я": "Тимко", "вік (міс)": 6})
        writer.writerow({"порода": "пікінес", "ім'я": "Лей", "вік (міс)": 2},)
#якщо файл не відкрився
except:
    print("Файл data.csv не знайдено!")
    
try:
    #відкриття файлу data.csv для зчитування даних
    with open('data.csv', 'r', encoding='utf-8') as csvfile:
        #відкриття файлу data.json для запису даних
        with open('data.json', 'w', encoding='utf-8') as jsonfile:
            #зчитування даних із файлу
            reader = csv.DictReader(csvfile, fieldnames)
            #запис даних у json файл
            for row in reader:
                json.dump(row, jsonfile, ensure_ascii=False)
                jsonfile.write('\n')                
#якщо файл не відкрився
except:
    print("Файл data.csv не знайдено!")

#Чернявська Анна КН-32-2
#Перетворення з json в csv
try:
    fieldnames = ["порода", "ім'я", "вік (міс)"]
    # Відкриття JSON файлу для зчитування
    with open('data.json', 'r', encoding='utf-8') as json_file:
        try:
            data = json.load(json_file)  # Завантаження даних із JSON файлу
        except json.JSONDecodeError:
            print("Файл data.json порожній або пошкоджений. Використовується порожній список.")
            data = []
except FileNotFoundError:
    print("Файл data.json не знайдено. Використовується порожній список.")
    data = []

# Додаємо нові записи
new_entries = [
    {"порода": "самоїд", "ім'я": "Біляш", "вік (міс)": 8},
    {"порода": "доберман", "ім'я": "Грета", "вік (міс)": 10}
]
data.extend(new_entries)

try:
    # Відкриття CSV файлу для запису
    with open('data.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        try:
            writer.writeheader()  # Запис заголовків
            writer.writerows(data)  # Запис рядків даних
            print("Дані успішно записані у data.csv")
        except csv.Error as e:
            print("Помилка під час запису в CSV файл:", e)
except IOError as e:
    print("Помилка доступу до CSV файлу:", e)
