def read_file(p):
    with open(p) as f:
        lines = f.readlines()
    return ''.join(lines)
