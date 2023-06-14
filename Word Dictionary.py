from PyDictionary import PyDictionary

dictionary=PyDictionary()

while True:
    word=input("Enter word: ")
    if word=="":
        break

    print(dictionary.meaning(word))

