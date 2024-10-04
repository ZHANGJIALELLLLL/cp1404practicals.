"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

get sales
while sales >= 0
    calculate bonus (this line is intentionally incomplete pseudocode)
    print bonus
    get sales
do next thing
"""
def calculate_bonus(sales):
    if sales >= 1000:
        return sales * 0.15
    else:
        return sales * 0.1
sales = float(input("Enter sales: $"))
while sales >= 0:
    bonus = calculate_bonus(sales)
    print(bonus)
    sales = float(input("Enter sales: $"))
print("Program ended.")



