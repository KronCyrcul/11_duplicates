import os
import sys


def get_all_files(path, all_files_dict):
    for current_path, folders_name, files_name in os.walk(path):
        for file_name in files_name:
            file_path = os.path.join(current_path, file_name)
            file_size = os.stat(file_path).st_size
            all_files_dict.setdefault((file_name, file_size), []).append(
                os.path.join(current_path, file_name))
    return all_files_dict


def check_duplicates(all_files_dict):
    duplicates = [duplicate_path for (duplicate_info, duplicate_path)
        in all_files_dict.items() if len(duplicate_path) >= 2]
    return duplicates


def print_duplicates(duplicates):
    if not bool(duplicates):
        print("Дубликаты не найдены")
    else:
        for duplicate_path_list in duplicates:
            print("Файлы по адресам {} являются дубликатами".format(
                ", ".join(duplicate_path_list)))


if __name__ == "__main__":
    try:
        main_path = sys.argv[1]
    except IndexError:
        sys.exit("Путь не найден")
    all_files_dict = {}
    if os.path.isdir(main_path):
        get_all_files(main_path, all_files_dict)
        duplicates = check_duplicates(all_files_dict)
        print_duplicates(duplicates)
    else:
        sys.exit("Неверный путь до папки")
