userInput = input()

if userInput.isdigit():
    for i in userInput:
        if i in "02356789":
            print("OOO", end = "  ")
        elif i in "1":
            print("  O", end = "  ")
        else :
            print("O O", end = "  ")
    print("")
    for i in userInput:
        if i in "0489":
            print("O O", end = "  ")
        elif i in "1237":
            print("  O", end = "  ")
        else :
            print("O  ", end = "  ")
    print("")
    for i in userInput:
        if i in "2345689":
            print("OOO", end = "  ")
        elif i in "17":
            print("  O", end = "  ")
        else :
            print("O O", end = "  ")
    print("")
    for i in userInput:
        if i in "134579":
            print("  O", end = "  ")
        elif i in "068":
            print("O O", end = "  ")
        else :
            print("O  ", end = "  ")
    print("")
    for i in userInput:
        if i in "0235689":
            print("OOO", end = "  ")
        else :
            print("  O", end = "  ")
else :
    print("Invalid input : Please input only the numbers")