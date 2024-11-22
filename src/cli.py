def read_str(prompt=""):
    """
    Get input from the console.
    :param prompt: The prompt
    :return: The input
    """
    return input(prompt)


def read_strs(separator, prompt=""):
    return read_str(prompt).split(separator)


def read_stripped_str(prompt=""):
    """
    Get input from the console. Strip the inputted value.
    :param prompt: The prompt
    :return: The stripped input
    """
    return read_str(prompt).strip()


def write_str(string):
    """
    Write a string to the console.
    :param string: The string
    """
    print(string)


def write_title_str(title):
    """
    Write a title string to the console.
    Title string is formed like f"=== {title} ===".
    :param title: The title
    """
    write_str(f"=== {title} ===")
