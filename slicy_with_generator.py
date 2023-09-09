def read_line_by_line (file_name):
    try:
        with open(file_name, 'r') as f:
            for line in f:
                yield(line.strip())
    except FileNotFoundError:
        print(f"file {file_name} not found")

for line in read_line_by_line('09092023.txt'):
    print(line[::-1])


