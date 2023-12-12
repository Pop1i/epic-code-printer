def read(file: str):
    try:
        with open(file, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "ERROR: FileNotFound"