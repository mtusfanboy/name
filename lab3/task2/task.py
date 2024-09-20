def write_data_to_file(
    file_path: str,
    file_mode: str,
    user_input: str,
):
    if not isinstance(file_path, str):
        print("Путь должен быть строкой")
        return
    try:
        with open(file_path, file_mode, encoding="UTF-8") as file:
            file.write(user_input)
    except FileNotFoundError:
        print("По заданному пути невозможно создать файл")
    except ValueError:
        print("Указан неверный режим открытия файла", file_mode)


if __name__ == "__main__":
    write_data_to_file(
        file_path="lab3/task2/user_input.txt",
        file_mode="a",
        user_input="Hello, World!"
    )
