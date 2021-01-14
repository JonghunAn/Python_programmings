year = int(input("연도를 입력하세요: "))

if(year%4==0 and year%100!=0):
    print(str(year)+"은 윤년입니다.")
else:
    if(year%400==0):
         print(str(year)+"은 윤년입니다.")
    else:
         print(str(year)+"은 윤년이 아닙니다.")