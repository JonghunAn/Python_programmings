name = input("사용자 이름을 입력하세요 : ")
call_amount = int(input("통화량(초)를 입력하세요 : "))
data_amount = int(input("데이터 사용량(MB)를 입력하세요 : "))

tot = (12100+(call_amount*1.98)+(data_amount*55))

print(name,"님의 이번달 요금 :",tot)
