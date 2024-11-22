def read_str(prompt=""):
    return input(prompt)


def read_stripped_str(prompt=""):
    return read_str(prompt).strip()


def write_str(string):
    print(string)


def write_title_str(title):
    write_str(f"=== {title} ===")
