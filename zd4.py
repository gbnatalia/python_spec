'''
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями. В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы функции.
'''

import csv
import json


def convert_csv_to_json(csv_file_path, json_file_path):
    with (open(csv_file_path, 'r', encoding="utf-8") as f_csv,
          open(json_file_path, 'w', encoding="utf-8") as f_json):
        reader = csv.reader(f_csv)
        header = next(reader)
        records = []
        for row in reader:
            id = row[0].zfill(10)
            name = row[1].capitalize()
            level = row[2]
            hash_field = hash(id + name)
            records.append({'id': id, 'name': name, 'level': level, 'hash': hash_field})
        json.dump(records, f_json)


if __name__ == "__main__":
    convert_csv_to_json('data3.csv', 'data4.json')
