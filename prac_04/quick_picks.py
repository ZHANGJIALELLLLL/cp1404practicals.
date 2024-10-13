import random
numbers_in_line = 6
min_number = 1
max_number = 45

def main():
    quick_picks_input = int(input("How many quick picks? "))
    for i in range(quick_picks_input):
        quick_picks = get_quick_picks_input()
        print_quick_picks(quick_picks)
def get_quick_picks_input():
    """Each line consists of 6 random numbers between 1 and 45."""
    numbers = []
    while len(numbers) < numbers_in_line:
        number = random.randint(min_number, max_number)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    return numbers

def print_quick_picks(quick_picks):
    print(" ".join(f"{number:2}" for number in quick_picks))

main()


