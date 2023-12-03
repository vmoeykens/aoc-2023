def part1(input_file="day2/input"):
    constraints = {"red": 12, "green": 13, "blue": 14}
    # Create a counter to increment with all games that are possible
    possible_game_score_count = 0
    # Open the input file and begin going line by line
    with open(input_file, "r") as f:
        for line in f:
            # Create a tracker to see if the game was possible
            game_possible = True
            # Split the line first on a colon
            split_line = line.split(":")
            # Pull the game ID from the first part of the split by getting the text after "Game "
            game_id = int(split_line[0].split("Game ")[1])
            # Split the second part of the split_line into sections divided by semicolons
            game_runs = split_line[1].split(";")
            # Iterate through the runs in the game and see if any aren't possible given the constraints
            for run in game_runs:
                # Split the run into the color and number pairs
                color_number_pairs = run.split(",")
                # Strip whitespace first from the color and number pairs
                color_number_pairs = [pair.strip() for pair in color_number_pairs]
                # Check each of the color number pairs to see if they match one of the keys in the constraint
                for pair in color_number_pairs:
                    for color_key in constraints.keys():
                        if color_key in pair:
                            # If the color is in the pair, check if the number is greater than the constraint
                            if int(pair.split(color_key)[0]) > constraints[color_key]:
                                # If the number is greater than the constraint, the game is not possible
                                game_possible = False
            if game_possible:
                # If the game is possible, increment the counter
                possible_game_score_count += game_id
    return possible_game_score_count

def part2(input_file="day2/input"):
    # Create a counter to increment with all games that are possible
    power_sum = 0
    # Open the input file and begin going line by line
    with open(input_file, "r") as f:
        for line in f:
            minimum_needed = {"red": 0, "green": 0, "blue": 0}
            # Split the line first on a colon
            split_line = line.split(":")
            # Split the second part of the split_line into sections divided by semicolons
            game_runs = split_line[1].split(";")
            # Iterate through the runs in the game and see if any aren't possible given the constraints
            for run in game_runs:
                # Split the run into the color and number pairs
                color_number_pairs = run.split(",")
                # Strip whitespace first from the color and number pairs
                color_number_pairs = [pair.strip() for pair in color_number_pairs]
                # Check each of the color number pairs to see if one of the colors is higher than the minimum needed
                for pair in color_number_pairs:
                    pair_split = pair.split(" ")
                    color = pair_split[1]
                    number = int(pair_split[0])
                    if number > minimum_needed[color]:
                        minimum_needed[color] = number
            # Get the power by multiplying the minimum needed for each color
            power = minimum_needed["red"] * minimum_needed["green"] * minimum_needed["blue"]
            # Add the power to the power sum
            power_sum += power
    return power_sum



def main():
    print(f'part1 test: {part1("day2/test_input")}')
    print(f'part1 actual: {part1()}')
    print(f'part2 test: {part2("day2/test_input")}')
    print(f'part2 actual: {part2()}')


if __name__ == "__main__":
    main()
