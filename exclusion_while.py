p=2; q=3
num = int(input("숫자를 입력해주세요 : "))
value=0
while(value<=num):
    value+=1
    if(value%p==0 and value%q==0):
        continue
       
    else:
        print(value)