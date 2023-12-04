import re
from collections import defaultdict
from math import prod

def make_grid(input_file):
    grid = []
    with open(input_file, "r") as f:
        for x_index, line in enumerate(f):
            grid.append([])
            for character in line:
                grid[x_index].append(character)
            grid[x_index].pop(-1)
    return grid        


def part1(input_file="day3/input"):
    part_number_sum = 0
    grid = make_grid(input_file)
    # Iterate through the grid and find any symbol that isn't a period
    # If the symbol isn't a period, check the 8 surrounding squares
    # If one of the surrounding squares is a number we need to extract the whole numeric value
    for x_index, row in enumerate(grid):
        temp_number = []
        has_symbol = False
        for y_index, character in enumerate(row):
            # setup indices
            left = (x_index - 1, y_index) if x_index != 0 else None
            right = (x_index + 1, y_index) if x_index != len(grid) - 1 else None
            up = (x_index, y_index - 1) if y_index != 0 else None
            down = (x_index, y_index + 1) if y_index != len(row) - 1 else None
            up_left = (x_index - 1, y_index - 1) if x_index != 0 and y_index != 0 else None
            up_right = (x_index + 1, y_index - 1) if x_index != len(grid) - 1 and y_index != 0 else None
            down_left = (x_index - 1, y_index + 1) if x_index != 0 and y_index != len(row) - 1 else None
            down_right = (x_index + 1, y_index + 1) if x_index != len(grid) - 1 and y_index != len(row) - 1 else None

            last_character = ''
            if character.isalnum():
                temp_number.append(character)
                # Check to see if any of the surrounding squares have a symbol
                if left:
                    if not grid[left[0]][left[1]].isalnum() and grid[left[0]][left[1]] != '.':
                        has_symbol = True
                if right:
                    if not grid[right[0]][right[1]].isalnum() and grid[right[0]][right[1]] != '.':
                        has_symbol = True
                if up:
                    if not grid[up[0]][up[1]].isalnum() and grid[up[0]][up[1]] != '.':
                        has_symbol = True
                if down:
                    if not grid[down[0]][down[1]].isalnum() and grid[down[0]][down[1]] != '.':
                        has_symbol = True
                if up_left:
                    if not grid[up_left[0]][up_left[1]].isalnum() and grid[up_left[0]][up_left[1]] != '.':
                        has_symbol = True
                if up_right:
                    if not grid[up_right[0]][up_right[1]].isalnum() and grid[up_right[0]][up_right[1]] != '.':
                        has_symbol = True
                if down_left:
                    if not grid[down_left[0]][down_left[1]].isalnum() and grid[down_left[0]][down_left[1]] != '.':
                        has_symbol = True
                if down_right:
                    if not grid[down_right[0]][down_right[1]].isalnum() and grid[down_right[0]][down_right[1]] != '.':
                        has_symbol = True
                last_character = character
            if (not character.isalnum() or (character.isalnum() and y_index == len(row) - 1)) and temp_number:
                # Check to see if we passed the last number, if so we combine temp number, add it to part_number_sum (if the flag that it was next to a character was true), and clear temp_number
                number = int(''.join(temp_number))
                if has_symbol:
                    part_number_sum += number
                temp_number = []
                has_symbol = False
    return part_number_sum


def part2(input_file="day3/input"):
    # solution partially scraped from reddit
    with open(input_file, "r") as f:
        lines = f.read().split("\n")

    # building symbols grid as {xy_position: symbol}
    symbols = dict()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c not in "1234567890.":
                symbols[(x, y)] = c

    # checking if a number has a rectangular neighborhood containing a symbol and
    # building a gear grid as {gear_position: [part numbers list]}
    gears = defaultdict(list)
    part_numbers_sum = 0
    for y, line in enumerate(lines):
        for match in re.finditer(r"\d+", line):
            for (s_x, s_y), c in symbols.items():
                if (match.start() - 1 <= s_x <= match.end()) and (y - 1 <= s_y <= y + 1):
                    num = int(match.group())
                    part_numbers_sum += num
                    if c == "*":
                        gears[(s_x, s_y)].append(num)
                    break
    return sum(prod(part_nums) for part_nums in gears.values() if len(part_nums) == 2)


def main():
    print(f'part1 test: {part1("day3/test_input")}')
    print(f'part1 actual: {part1()}')
    print(f'part2 test: {part2("day3/test_input")}')
    print(f'part2 actual: {part2()}')


if __name__ == "__main__":
    main()
