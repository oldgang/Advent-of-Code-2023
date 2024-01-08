import re

def convert_to_int(number):
    numbers = [ '1', '2', '3', '4', '5', '6', '7', '8', '9',
            'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    id = numbers.index(number)
    if id < 9:
        return int(numbers[id])
    return int(numbers[id-9])

# Find all numbers in the line and return a dictionary containing {number: span} or {number: [span0, ..., spanX]} pairs
def find_numbers(line):
    numbers = [ '1', '2', '3', '4', '5', '6', '7', '8', '9',
                'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    found = {}
    # Find all numbers and their spans in lines
    for number in numbers:
        res = re.finditer(number, line)
        for match in res:
            if number not in found.keys():
                found[number] = match.span()
            else:
                # if the number is already in the dictionary, add the span to the list
                values = found[number]
                if type(values) != list:
                    values = [values]
                values.append(match.span())
                found[number] = values

    return found

# Calculate the calibration value stored in the line
def calculate_value(line):
    found = find_numbers(line)
    # Find the first and last number in the text
    firstIndex = 10000000
    firstNumber = ''
    lastIndex = 0
    lastNumber = ''
    for key in found.keys():
        if type(found[key]) == list:
            for span in found[key]:
                start, end = span
                if start < firstIndex:
                    firstIndex = start
                    firstNumber = key
                if end > lastIndex:
                    lastIndex = end
                    lastNumber = key
        else:
            start, end = found[key]
            if start < firstIndex:
                firstIndex = start
                firstNumber = key
            if end > lastIndex:
                lastIndex = end
                lastNumber = key

    # calculate the sum of the first and last number
    numbers = (convert_to_int(firstNumber), convert_to_int(lastNumber))
    value = int(str(numbers[0]) + str(numbers[1]))
    return value

# with open('1/example.txt' , 'r') as f:
#     lines = f.readlines()
#     lines = [line.strip() for line in lines]

with open('1/input.txt' , 'r') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

sum = 0
for line in lines:
    sum += calculate_value(line)
print(sum)