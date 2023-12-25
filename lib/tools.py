
def read_input(filename): 
    rows = []
    with open(filename) as f:
        data = f.readlines()
    for line in data:
        line = line.strip()
        rows.append(line)
    return rows
