import numpy as np
import time

start_time = time.time()


def process(file_name):
    # Definition
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

    # Load file
    with open(file_name, "r") as data_file:
        data_lines = data_file.readlines()

    def get_value_for_line(line):
        numbers = [x for x in list(line.strip()) if str.isdigit(x)]
        return int(numbers[0] + numbers[-1]) if numbers else 0

    def parse_text_numbers(line):
        for idx, text in enumerate(text_numbers):
            line = line.replace(text, f"{text}{idx + 1}{text}")
        return line

    total_1 = np.sum([get_value_for_line(line) for line in data_lines])
    total_2 = np.sum(
        [get_value_for_line(parse_text_numbers(line)) for line in data_lines]
    )

    print(f"{file_name}: {total_1}, {total_2}")


process("01/test.dat")
process("01/test2.dat")
process("01/input.dat")

print("Executed in", time.time() - start_time)

exit()
