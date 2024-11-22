UTF_8 = "utf-8"


def read(file):
    """
    Open the file with UTF-8 encoding and return its whole content (using .read()).
    Print an error message if an IO exception is encountered.
    FileNotFound exceptions are not handled, but raised.
    :param file: The file to read
    :return: File content
    """
    try:
        with open(file, encoding=UTF_8) as f:
            return f.read()
    except FileNotFoundError as e:
        raise e
    except IOError:
        print(f"Unexpected error reading file {file}.")


def write(file, content):
    """
    Open the file with UTF-8 encoding and write the content to it, overrides presiouse content.
    Print an error message if an IO exception is encountered.
    :param file: The file to write to
    :param content: The content to write
    """
    try:
        with open(file, "w", encoding=UTF_8) as f:
            f.write(content)
    except IOError:
        print(f"Unexpected error writing file {file}.")
