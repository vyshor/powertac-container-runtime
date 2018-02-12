def open_read_close(path) -> str:
    f = open(path)
    c = f.read()
    f.close()
    return c