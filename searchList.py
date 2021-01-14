number=[]

while True :
    print("Enter numbers. (To finish press 'Enter' key)")
    n = input()
    if len(n) ==0 :
        break
    number.append(float(n))

number.sort()
number_len = len(number)

midNum = int(number_len/2)

if(midNum%2==0):
    median = number[midNum] 
else:
    median = (number[midNum-1]+number[midNum])/2 

print("You entered\n",number)
print("max : %.1f" %number[-1])
print("min : %.1f" %number[0])
print("median : %.2f" %median)
