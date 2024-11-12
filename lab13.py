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
