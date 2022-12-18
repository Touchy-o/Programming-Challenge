userInput = input()

numText = {
    0 : "ZERO",
    1 : "ONE",
    2 : "TWO",
    3 : "THREE",
    4 : "FOUR",
    5 : "FIVE",
    6 : "SIX",
    7 : "SEVEN",
    8 : "EIGHT",
    9 : "NINE"
}

if userInput.isdigit():
    for i in userInput:
        print(numText[int(i)], end = " ")
else:
    print("Invalid input : Please input only the numbers")