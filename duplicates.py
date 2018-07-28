import os
import sys
from stat import S_ISDIR, S_ISREG


def get_all_files(path, all_files_dict):
    dir_files = os.listdir(path)
    for file in dir_files:
        file_path = os.path.join(path, file)
        file_stats = os.stat(file_path)
        if S_ISDIR(file_stats.st_mode):
            get_all_files(file_path, all_files_dict)
        elif S_ISREG(file_stats.st_mode):
            all_files_dict[file_path] = [file, file_stats.st_size]
        else:
            pass
    return all_files_dict


def check_duplicates(all_files_dict):
    duplicates = [path for (path, file_info) in all_files_dict.items()
        if list(all_files_dict.values()).count(file_info) >= 2]
    if not bool(duplicates):
        sys.exit("Дубликаты не найдены")
    return duplicates


def print_duplicates(duplicates):
    for duplicate in duplicates:
        print("Файл по адресу {} имеет дубликат"
            " в проверяемой папке".format(duplicate))

if __name__ == "__main__":
    try:
        main_path = sys.argv[1]
        all_files_dict = {}
        if os.path.isdir(main_path):
            get_all_files(main_path, all_files_dict)
            duplicates = check_duplicates(all_files_dict)
            print_duplicates(duplicates)
        else:
            sys.exit("Неверный путь до папки")
    except IndexError:
        sys.exit("Путь не найден")
