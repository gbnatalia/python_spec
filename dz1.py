'''
Задача не решенная на семинаре
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
'''
from pathlib import Path
import os
import shutil

def sort_files(folder_path):
    video_extensions = ['mp4', 'avi', 'mkv']
    image_extensions = ['jpg', 'jpeg', 'png']
    text_extensions = ['txt', 'doc', 'docx']

    for file in Path(folder_path).iterdir():

        file_path = Path(folder_path / file)
        ext = Path(file).suffix

        if ext[1:] in video_extensions:
            target_dir = Path(folder_path / 'VIDEO')
        elif ext[1:] in image_extensions:
            target_dir = Path(folder_path / 'IMAGE')
        elif ext[1:] in text_extensions:
            target_dir = Path(folder_path / 'TEXT')
        else:
            continue

        if not os.path.exists(target_dir):
            Path(target_dir).mkdir()

        shutil.move(file_path, target_dir)

    print('Файлы отсортированы!')

if __name__ == "__main__":
    sort_files(Path(Path().cwd().parent/"FILES"))