userInput = input().lower() + " "

vowels = ""
count = 0
isVowels = False

for i in userInput:
    if i in "aeiou":
        vowels += i
        isVowels = True
    else :
        if isVowels:
            print(vowels, end = " ")
            count += 1
            isVowels = False
            vowels = ""

if count == 0:
    print("0")
else :
    print("=", count)