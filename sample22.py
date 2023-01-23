story = ""
word = input("Please type in a word: ")
previous_word = ""
flag = False
while word != "end":
    if word == previous_word:
        print(story)
        flag = True
        break
    else:
        story += word + " "
    previous_word = word
    word = input("Please type in a word: ")
if flag == False:
    print(story)