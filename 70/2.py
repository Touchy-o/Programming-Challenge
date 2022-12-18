userInput = input().lower()

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
print("=", count)