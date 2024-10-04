import random

def evaluate_score(score):
    """Evaluates the score and returns the result as a string."""
    if score > 100 or score < 0:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"

def main():
    user_score = float(input("Enter score: "))
    result = evaluate_score(user_score)
    print(result)

    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}")
    random_result = evaluate_score(random_score)
    print(random_result)


main()