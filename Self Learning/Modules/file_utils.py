# File utility module

def read_file(path):
    """Read file"""
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        return "File not found"


def write_file(path, content):
    """Write file"""
    with open(path, "w") as f:
        f.write(content)


def append_file(path, content):
    """Append file"""
    with open(path, "a") as f:
        f.write(content)


def count_lines(path):
    """Count lines"""
    try:
        with open(path) as f:
            return len(f.readlines())
    except FileNotFoundError:
        return 0


def count_words(path):
    """Count words"""
    try:
        with open(path) as f:
            return len(f.read().split())
    except FileNotFoundError:
        return 0