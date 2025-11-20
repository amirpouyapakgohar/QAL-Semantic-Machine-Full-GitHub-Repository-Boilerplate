def decode(line):
    parts = line.strip().split()
    op = parts[0]
    args = "".join(parts[1:]).split(",")

    return op, args
