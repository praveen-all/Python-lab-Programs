# koch snowflake
import turtle

def koch_snowflake(t,x1,y1,x2,y2,depth):
    if depth==0:
        t.penup()
        t.goto(x1,y1)
        t.pendown()
        t.goto(x2,y2)
    else:
        xa=x1+(x2-x1)/3
        ya=y1+(y2-y1)/3
        xb=x1+2*(x2-x1)/3
        yb=y1+2*(y2-y1)/3
        xc=(x1+x2)/2-(y2-y1)*(3**0.5)/6
        yc=(y2+y1)/2+(x2-x1)*(3**0.5)/6
        
        koch_snowflake(t,x1,y1,xa,ya,depth-1)
        koch_snowflake(t,xa,ya,xc,yc,depth-1)
        koch_snowflake(t,xc,yc,xb,yb,depth-1)
        koch_snowflake(t,xb,yb,x2,y2,depth-1)
        
        
t=turtle.Turtle()
size=300
depth=2
x1=-size/2
y1=(size)*(3**0.5)/6
x2=size/2
y2=(size)*(3**0.5)/6   
x3=0
y3=-(size)*(3**0.5)/6

koch_snowflake(t,x1,y1,x2,y2,depth)
koch_snowflake(t,x2,y2,x3,y3,depth)
koch_snowflake(t,x3,y3,x1,y1,depth)


turtle.done()

        