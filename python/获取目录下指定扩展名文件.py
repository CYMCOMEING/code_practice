import os


def get_files(dir, type=None):
    fi = os.listdir(dir)
    file_list = []
    for file in fi:
        if type and (os.path.splitext(file)[1] in type):
            file_list.append(file)
        elif not type:
            file_list.append(file)

    return file_list


if __name__ == "__main__":
    print(get_files('.', ['.txt', '.py']))
