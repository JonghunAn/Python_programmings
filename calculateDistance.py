import math

x1 = int(input("x1 :"))
y1 = int(input("y1 :"))
x2 = int(input("x2 :"))
y2 = int(input("y2 :"))

res = math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))
print("두점 사이의 거리 :",res);
