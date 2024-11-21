UTF_8 = "utf-8"


def read(file):
    try:
        with open(file, encoding=UTF_8) as f:
            return f.read()
    except FileNotFoundError as e:
        raise e
    except IOError:
        print(f"Unexpected error reading file {file}.")


def write(file, content):
    try:
        with open(file, "w", encoding=UTF_8) as f:
            f.write(content)
    except IOError:
        print(f"Unexpected error writing file {file}.")
