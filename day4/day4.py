def part1(input_file='input'):
    total_points = 0
    with open(input_file) as f:
        for line in f:
            current_points = 0
            # Split line on :
            # First part is the title
            # Second part is the game
            title, values = line.split(':')
            winning_values, our_values = values.split('|')
            # Strip whitespace and split on where there was whitespace
            winning_values_list = winning_values.split()
            our_values_list = our_values.split()
            # Iterate through our values list and see if any match winning values
            # If they do we start counting points
            for value in our_values_list:
                if value in winning_values_list:
                    if current_points == 0:
                        current_points += 1
                    else:
                        current_points *= 2
            total_points += current_points
    return total_points


def process_cards(original_card_list, card_list, current_points):
    to_process_list = []
    if len(card_list) == 0:
        return current_points + len(original_card_list)
    for index, card in enumerate(card_list):
        card_matches = 0
        for value in card[2]:
            if value in card[1]:
                card_matches += 1
                current_points += 1
        for i in range(card_matches):
            card_index = card[0].split()[1]
            card_index_offset = int(card_index) + i
            to_process_list.append(original_card_list[card_index_offset])
    return process_cards(original_card_list, to_process_list, current_points)


def part2(input_file='input'):
    card_list = []
    with open(input_file) as f:
        for line in f:
            current_points = 0
            # Split line on :
            # First part is the title
            # Second part is the game
            title, values = line.split(':')
            winning_values, our_values = values.split('|')
            # Strip whitespace and split on where there was whitespace
            winning_values_list = winning_values.split()
            our_values_list = our_values.split()
            # Add a three-tuple to our list
            # (title, winning_values_list, our_values_list)
            card_list.append((title, winning_values_list, our_values_list))
    return process_cards(card_list, card_list, 0)


def main():
    print(f'part1 test: {part1("test_input")}')
    print(f'part1: {part1()}')
    print(f'part2 test: {part2("test_input")}')
    print(f'part2: {part2()}')


if __name__ == '__main__':
    main()
