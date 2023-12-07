#!/bin/bash

for day in {1..25}; do
    day_dir="day$day"
    python_file="$day_dir/day$day.py"

    # Check if directory exists, if not, create it
    if [ ! -d "$day_dir" ]; then
        mkdir "$day_dir"
    fi

    # Create Python script
    echo "def part1(input_file='input'):" > "$python_file"
    echo "    pass" >> "$python_file"
    echo "" >> "$python_file"
    echo "" >> "$python_file"
    echo "def part2(input_file='input'):" >> "$python_file"
    echo "    pass" >> "$python_file"
    echo "" >> "$python_file"
    echo "" >> "$python_file"
    echo "def main():" >> "$python_file"
    echo "    print(f'part1 test: {part1(\"test_input\")}')" >> "$python_file"
    echo "    print(f'part1: {part1()}')" >> "$python_file"
    echo "    print(f'part2 test: {part2(\"test_input\")}')" >> "$python_file"
    echo "    print(f'part2: {part2()}')" >> "$python_file"
    echo "" >> "$python_file"
    echo "" >> "$python_file"
    echo 'if __name__ == "__main__":' >> "$python_file"
    echo "    main()" >> "$python_file"

    # Create input files
    touch "$day_dir/input"
    touch "$day_dir/test_input"
done
