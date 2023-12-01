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
                print(int(f'{first}{last}'))
                total += int(f'{first}{last}')
            else:
                print("No numbers found in input file")
    print(total)


def part2():



def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
