menu = 0
words =[]
word =""

def print_menu() :
    print("*"*40)
    print("%-40s"%"*         Sookmyung Dictionary         *")
    print("*"*40)
    
    print("*\t 1. Save words")
    print("*\t 2. Delete a word")
    print("*\t 3. Print all the words")
    print("*\t 4. Exit")
    print("="*40)

while (True) :
    print_menu()
    select = int(input("Select menu >> "))
    
    if(select==1):
        print("Enter words to save (Press 'Enter' key to finish)\n")
        while(True):
            word = input("Word: ")
            if(word ==""):
                break
            elif(word in words):
                print("already exists")
            else:
                words.append(word)
    
    elif(select==2):
            print("Enter a word to delete\n")
            
            while(True):
                word = input("Word: ")
        
                if(word =="\n"):
                    break
                elif(word not in words):
                    print("doesn't exist")
                else:
                    words.remove(word)
                    print()
                    break

    elif(select==3):
        print()
        for i in range(len(words)):
            print(words[i])
        print()
    elif(select==4):
        break
    else:
        print("wrong menu\n")


