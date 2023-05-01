'''
Напишите функцию, которая получает на вход директорию и
рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.

Для дочерних объектов указывайте родительскую директорию.
Для каждого объекта укажите файл это или директория.
Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней
с учётом всех вложенных файлов и директорий.
'''
import os
import json
import csv
import pickle


def save_results_to_file(results, directory):
    json_file_path = os.path.join(directory, 'results.json')
    csv_file_path = os.path.join(directory, 'results.csv')
    pickle_file_path = os.path.join(directory, 'results.pickle')

    with open(json_file_path, 'w') as f:
        json.dump(results, f)

    with open(csv_file_path, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'type', 'path', 'size'])
        for obj in results:
            writer.writerow([
                obj['name'],
                obj['type'],
                obj['path'],
                obj['size']
            ])

    with open(pickle_file_path, 'wb') as f:
        pickle.dump(results, f)


def print_result(results):
    print(f"{'-' * 121}")
    print(f"| {'Имя объекта':^30} | {'Тип':^10} | {'директория':^60} | {'размер':^8} |")
    print(f"{'-' * 121}")
    for result in results:
        print(f"| {result['name']:<30} | {result['type']:^10} | {result['path']:<60} | {result['size']:8} |")
    print(f"{'-' * 121}")


def get_directory_size(directory):
    size = 0
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            size += os.path.getsize(fp)
    return size


def walk_directory_(directory):

    results = []

    for dirpath, dirs, files in os.walk(directory):

        path = files
        path.extend(dirs)

        for name in path:

            fullname = os.path.join(dirpath, name)
            is_file = os.path.isfile(fullname)
            result = {
                'name': name,
                'type': 'file' if is_file else 'directory',
                'path': dirpath,
            }
            if is_file:
                result['size'] = os.path.getsize(fullname)
            else:
                result['size'] = get_directory_size(fullname)

            results.append(result)

    return results


def save_directory_results(directory):
    results = walk_directory_(directory)
    print_result(results)
    save_results_to_file(results, directory)


if __name__ == "__main__":
    from pathlib import Path
    save_directory_results(Path().cwd().parent)
