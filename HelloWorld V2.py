import time
import string

Chars = list(" "+string.ascii_letters+"0"+"1"+"2"+"3"+"4"+"5"+"6"+"7"+"8"+"9")
word = input("Enter the word you wish to find:\n")
finishedwork = ""
loopLen = len(word)

for i in range(loopLen):
    searchLet = Chars[0]
    wordlet = word[i]
    looped = 0
    while (searchLet != wordlet):
        searchLet = Chars[looped]
        looped+=1
        print(finishedwork + searchLet)
        time.sleep(0.03)
    finishedwork += searchLet
