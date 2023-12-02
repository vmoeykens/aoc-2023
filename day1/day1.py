import re

def part1():
    # Read input from file called "input"
    with open("day1/input", "r") as f:
        # Create a total counter
        total = 0
        # Iterate through lines and find the first and last elements that are a number
        for line in f:
            first = None
            last = None
            for character in line:
                if character.isdigit():
                    if not first:
                        first = character
                    last = character
            # Sum the first and last values if we have any
            if first and last:
                # print(int(f'{first}{last}'))
                total += int(f'{first}{last}')
            else:
                print("No numbers found in input file")
    print(total)


def part2():
    VALID_NAMES = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    # Read input from file called "input"
    with open("day1/input", "r") as f:
        # Create a total counter
        total = 0
        # Iterate through lines and find the first and last elements that are a number
        for line in f:
            # Create dict mapping indices to numbers
            number_map = {}
            first = None
            last = None
            for index, character in enumerate(line):
                if character.isdigit():
                    number_map[index] = character
            for name in VALID_NAMES.keys():
                if name in line:
                    indices = [m.start() for m in re.finditer(name, line)]
                    for index in indices:
                        number_map[index] = VALID_NAMES[name]
            # Find the smallest numeric key in the number_map
            if number_map:
                first = number_map[min(number_map.keys())]
                last = number_map[max(number_map.keys())]

            # Sum the first and last values if we have any
            if first and last:
                # print(int(f'{first}{last}'))
                total += int(f'{first}{last}')
            else:
                print("No numbers found in input file")
    print(total)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
