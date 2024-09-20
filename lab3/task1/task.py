def write_file(file_path: str):
    if not isinstance(file_path, str):
        print("Путь должен быть строкой")
        return
    try:
        with open(file_path, "w", encoding="UTF-8") as file:
            file.write("This is the first line.\n")
            file.write("Here is the second line.\n")
            file.write("And this is the third line.\n")
    except FileNotFoundError:
        print("По заданному пути невозможно создать файл")


def read_file(file_path: str):
    if not isinstance(file_path, str):
        print("Путь должен быть строкой")
        return
    try:
        with open(file_path, "r", encoding="UTF-8") as file:
            return file.read()
    except FileNotFoundError:
        print("По заданному пути невозможно прочитать файл")


def read_file_methods(file_path: str, method="all"):
    if not isinstance(file_path, str):
        print("Путь должен быть строкой")
        return
    """
    Args:
        file_path (str): Path to txt file
        method (str, optional): _description_. Defaults to "all".
        all - read all file
        lines - read file by lines

    Returns:
        result (tuple): Selected method and file content
    """
    try:
        with open(file_path, "r", encoding="UTF-8") as file:
            if method == "all":
                # Чтение всего файла сразу
                content = file.read()

            elif method == "lines":
                # Чтение построчно
                content = ""
                for line in file:
                    content += line
            else:
                return "ERROR: This method is unsupported"
            return method, content
    except FileNotFoundError:
        print("По заданному пути невозможно прочитать файл")


if __name__ == "__main__":
    write_file("lab3/task1/example.txt")
    print(read_file("lab3/task1/example.txt"))
    print(read_file_methods("lab3/task1/example.txt", "all"))
