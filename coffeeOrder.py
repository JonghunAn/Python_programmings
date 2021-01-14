
menu=["아메리카노","카페라떼","카페모카"]
price=[1800,2200,2800]
number=1
print("\t=====Sookmyung Cafe=====")
for i in menu:
    for j in price:
        print("\t   %d.%s %d원"%(number,i,j))
        number+=1
        break
print("\t========================")

menu_num =0
num =0
exit =False
tot_num =0
tot_price =0
order_list =[]
while(exit==False):
    menu_num = int(input("\n메뉴를 선택해주세요 >>> "))
    if(menu_num>3 or menu_num<1):
        print("메뉴를 다시 선택해주세요")
        while(menu_num>3 and menu_num<1):
            menu_num = int(input("메뉴를 선택해주세요 >>> "))
    else:
        num = int(input("몇 잔을 주문하시겠습니까? >>> "))
    
        order_list.append([menu_num,num])
        tot_num+=num
        tot_price+=(price[menu_num-1]*num)
    
        keep = input("주문을 계속 하시겠습니까?(Y/N) >>> ")

        if(keep=='y' or keep=='Y'):
            continue
        elif(keep=='N' or keep=='n'):
            exit=True

print("\n=====주 문 내 역=====")

for i,j in order_list:
        print("  %s %d잔"%(menu[i-1],j))

print("\n==총 %d잔, %d원=="%(tot_num,tot_price))
print("\n이용해주셔서 감사합니다.")
