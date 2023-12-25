# Part 1
def calculate_sum(lines):
    sum = 0
    for line in lines:
        values = [c for c in line if c.isdigit()]
        if len(values) < 2:
            sum += int(values[0] + values[0])
            continue
        sum += int(values[0] + values[-1])
    return sum

# Part 2
def parse_input(lines):
    pass


with open('1/input.txt', 'r') as f:
    lines = f.readlines()
    print(calculate_sum(lines))