COLOR_TO_HEX = {"Absolute Zero": "#0048ba",
                "Black": "#000000",
                "Arylide Yellow": "#e9d66b",
                }
print(COLOR_TO_HEX)
state_code = input("Enter color: ").strip().capitalize()

while state_code != "":
    if state_code in COLOR_TO_HEX:
        print(state_code, "is", COLOR_TO_HEX[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter color: ").strip().capitalize()