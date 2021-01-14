import easygui,turtle,math

shape = easygui.buttonbox("모양을 선택하세요.",choices=["circle","rectangle"])
num = int(easygui.enterbox("개수를 입력하세요."))

turtle.setup(800,800)
t = turtle.Pen()
iter=0
if(shape =="circle"):
        while(iter<num):
            t.down()
            t.circle(20)
            iter+=1
            t.up()
            t.forward(40)
elif(shape=="rectangle"):
    k=0
    while(iter<num):
        k=0
        t.up()
        t.forward(20)
        iter+=1
        while(k<4):
            t.down()
            t.forward(20)
            t.right(90)
            k+=1
        
            
            
    