import easygui

words = []
line = easygui.enterbox("Write a sentence")
easygui.msgbox("You wrote \"%s\""%line)
words = line.split()
select = easygui.choicebox("Choose your word to study",choices=words)
easygui.msgbox("Today's word :\n%s"%select)
