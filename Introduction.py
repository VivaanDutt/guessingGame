# intro = input("Introduce youself!")
# print(intro)
# wordCount = 0
# characterCount = 0
# for i in intro:
#     characterCount += 1
#     print(characterCount)
#     if (i == " "):
#         wordCount += 1
# print(wordCount + 1)

def countwords():
    fileName = input("Enter your file")
    openText = open(fileName, "r")
    readopentext = openText.readlines()
    for line in readopentext:
        words = line.split()
        print(line)
        print(words)

countwords()