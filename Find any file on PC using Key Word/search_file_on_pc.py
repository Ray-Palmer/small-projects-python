import os
import shutil

KEY_FOR_SEARCH = input("Enter what needs to be found?\n")
PATH_TO_COPY = input("Where to copy the files?\n")


def search():
    for adress, dirs, files in os.walk(input("Where to start?\n")):
        if adress == PATH_TO_COPY:
            continue
        for file in files:
            if file.endswith('.txt') and '$' not in file:
                yield os.path.join(adress, file)


def read_from_path_txt(path):
    with open(path) as file:
        for raw in file:
            if KEY_FOR_SEARCH in raw:
                return copy(path)


def copy(path):
    file_name = path.split('\\')[-1]

    counter = 1
    while True:
        if os.path.isfile(os.path.join(PATH_TO_COPY, file_name)):
            if f'({counter - 1})' in file_name:
                file_name = file_name.replace(f'({counter - 1})', '')
            file_name = f'({counter}).'.join(file_name.split('.'))
            counter += 1
        else:
            break

    shutil.copyfile(path, os.path.join(PATH_TO_COPY, file_name))
    print("File successfully copied:", file_name)


def main():
    for path in search():
        try:
            read_from_path_txt(path)
        except Exception as error:
            with open(os.path.join(PATH_TO_COPY, 'errors_log.txt'), 'a') as output:
                output.write(str(error) + '\n' + path + '\n' * 2)
    print("All copied! Have a good day...")


if __name__ == '__main__':
    main()
