import sys
import numpy


def process(file_name):
    # definition
    text_numbers = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    # load file
    data_file = open(file_name, "r")
    data_lines = data_file.readlines()

    def value_for_line(line):
        numbers = [x for x in list(line.strip()) if str.isdigit(x)]
        return int(numbers[0] + numbers[-1] if len(numbers) > 0 else 0)

    def parse_text_numbers(line):
        for idx, text in enumerate(text_numbers):
            line = line.replace(text, text + str(idx + 1) + text)
        return line

    print(
        file_name,
        numpy.sum([value_for_line(line) for line in data_lines]),
        numpy.sum([value_for_line(parse_text_numbers(line)) for line in data_lines]),
    )


process("01/test.dat")
process("01/test2.dat")
process("01/input.dat")
exit()
