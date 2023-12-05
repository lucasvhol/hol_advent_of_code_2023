import re

# Part 1: Extract Calibration Value
file_path = "input.txt"  # Specify the path to your local file here
with open(file_path, "r") as file:
    calibration_data = [line.strip() for line in file]

def extract_calibration_value(line):
    digits = re.findall(r'\d', line)
    return int(digits[0] + digits[-1]) if digits else 0

# Part 2: Find All Numbers with Positions
number_words_to_digits = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
}

def find_all_numbers_with_positions(s, number_words):
    result = {}
    pattern = r'\b(' + '|'.join(number_words.keys()) + r')\b|\d'
    for match in re.finditer(pattern, s):
        word = match.group()
        if word.isdigit() or word in number_words:
            result.setdefault(word, []).append(match.start())
    return result

total_calibration_value = sum(extract_calibration_value(line) for line in calibration_data)
print(f"Solution: {total_calibration_value}")
