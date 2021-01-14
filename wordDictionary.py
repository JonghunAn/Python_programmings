menu = 0
words =[]
meanings =[]
word =""
meaning=""
score =0
rank =[]

def print_menu() :
    print("*"*40)
    print("%-40s"%"*         Sookmyung Dictionary         *")
    print("*"*40)
    
    print("*\t 1. Save words")
    print("*\t 2. Print all the words")
    print("*\t 3. Delete a word")
    print("*\t 4. Search a word")
    print("*\t 5. Word Test")
    print("*\t 6. Word Test Score")
    print("*\t 7. Exit")
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
                meaning = input("Meaning: ")
                words.append(word)
                meanings.append(meaning)
    
    elif(select==2):
        print()
        for i in range(len(words)):
            print(words[i]+"\t"+meanings[i])
        print()

    elif(select==3):
          word = input("Enter a word to delete: ")
    
          if(word not in words):
              print("doesn't exist; detection failed!\n")
          else:
              index = words.index(word)
              words.remove(word)
              del meanings[index]
              print()

    elif(select==4):
         word = input("Enter a word to search: ")
         if(word in words):
              print(word+"\t"+meanings[words.index(word)]+"\n")
         else:
             print("doesn't exist; search failed!\n")
    
    elif(select==5):
        score=0
        for i in range(len(words)):
            answer = input(words[i]+": ")
            if(answer == meanings[i]):
                print("\nCorrect!")
                score+=1
            else:
                print("\nWrong...")
            
            if(i == len(words)-1):
                print("\nTest score: %d\n"%score)
                rank.append(score)
        
    elif(select==6):
        rank.sort(reverse=True)
        print("\n  Scoreboard  ")
        print("="*14)
        for i in range(len(rank)):
            print("rank %d score: %d"%(i+1,rank[i]))

    elif(select==7):
        break
    else:
        print("wrong menu\n")
