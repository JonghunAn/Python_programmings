tot =100000
menu =0
iterate=False

print("================================")
print("     은행 ATM")
print("================================")
name = input("계좌 소유주의 이름을 입력해주세요 : ")

while(True):
    if(iterate==True):
        print("\n================================")
        print("     은행 ATM")
        print("================================")
       
    iterate=True
    print("1.입금\n2.출금\n3.잔액확인\n4.종료")
    print("================================")

    menu = int(input("메뉴선택 : "))
    if(menu==1):
        money = int(input("입금할 금액을 입력해주세요 : "))
        if(money>0):
            tot+=money
            print("%s원이 정상적으로 입금되었습니다."%money)
        else:
            print("\n정확한 금액을 입력해주세요\n")

    elif(menu==2):
        money = int(input("출금할 금액을 입력해주세요 : "))
        if(money>0) and tot>=money:
            tot-=money
            print("%s원이 정상적으로 출금되었습니다."%money)
        elif(money<=0):
            print("\n정확한 금액을 입력해주세요")
        elif(tot<money):
            print("\n잔액부족. 거래가 거절되었습니다.")

    elif(menu==3):
        print(name+"님의 현재 잔액은 "+str(tot)+"원입니다.")

    elif(menu==4):
        print("저희 은행을 이용해주셔서 감사합니다.")
        break
    else:
        print("1-4 사이의 메뉴를 선택해주세요")
