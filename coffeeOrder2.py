catalog = {"아메리카노":1800,"카페라떼":2200,"카페모카":2800}
order = {"아메리카노":0,"카페라떼":0,"카페모카":0}
task = 0

def selectTask():
    print("=====Sookmyung Cafe=====")
    print("   1.주문접수\n   2.주문 내역 확인   \n   3.결제 처리")
    print("========================")
    
    task = int(input("\n작업을 선택해주세요>>"))
    return task

def displayCatalog(catalog):
    print("[Cafe Menu]")
    for key,value in catalog.items():
        print("{key} {value}".format(key=key,value=value),end="\n")

def getOrder(catalog,order):
    displayCatalog(catalog)
    
    while(True):
        select = input("\n커피를 선택해주세요 (Enter 입력 시 종료) >>> ")
        if(select ==""):
            break
        elif(select in catalog):
         num = int(input("몇 잔을 주문하시겠습니까? >>"))
         order[select] += num
        elif(select not in catalog):
         print("없는 커피입니다.")

    return order

def displayOrder(order):
     print("주문 내역은 다음과 같습니다.")
     
     for key in catalog: 
        num = int(order.get(key)) 
        if(num!=0):   
            print(key+" "+str(order.get(key))+"잔")

def calculatePrice(catalog,order):
    index=0
    sum =0
    for menu,price in catalog.items():
        sum += (int(price)*int(order[menu]))
        index+=1
    return sum

def processPayment(catalog,order):
    tot_price = calculatePrice(catalog,order)
    print("%d원 나왔습니다"%tot_price)
    while(True):
        get_money = int(input("지불금액 >>>"))
        
        if(get_money>=tot_price):
            change_price = get_money-tot_price
            break
        else:
            print("지불할 금액이 주문 금액보다 적습니다\n")
        
    print("거스름돈은 %d원입니다."%change_price)
    print("\n이용해주셔서 감사합니다.")

while True:
    task = selectTask()

    if task ==1:
        order = getOrder(catalog,order)
    elif task ==2:
        displayOrder(order)
    elif task ==3:
        processPayment(catalog,order)
        break
    else:
        print("잘못된 작업 번호입니다.\n")



