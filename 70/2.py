userInput = input().lower() + " "

vowels = ""
count = 0

for i in userInput:
    if i in "aeiou":
        vowels += i
    elif vowels:
        print(vowels, end = " ")
        count += 1
        vowels = ""

if count == 0:
    print("0")
else:
    print("=", count)