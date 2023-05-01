'''
Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
'''
import csv
import json

def json_to_csv(json_file_path, csv_file_path):

    with (open(json_file_path, "r", encoding="utf-8") as f_json,
          open(csv_file_path, "w", encoding="utf-8", newline="") as f_csv):

        # чтение данных
        data = json.load(f_json)

        # Запись данных
        writer = csv.writer(f_csv)
        writer.writerow(['Идентификатор', 'Имя', 'Уровень допуска'])
        for level, users in data.items():
            for name, identifier in users.items():
                writer.writerow([identifier, name, level])

if __name__ == "__main__":
    json_to_csv("data2.json", "data3.csv")
