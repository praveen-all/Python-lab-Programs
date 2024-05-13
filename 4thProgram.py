# Develop a program using Turtle graphic, write a program that asks the user for the number of sides, the length of the side, the colour, and the fill colour of a regular polygon. The program should draw the polygon and then fill it in.
import turtle

num_sides=int(input("Enter the number of sides:\n"))
side_len=int(input("length of each side:\n"))
pen_color=input("Enter the pen color:\n")
fill_color=input("Enter the fill color: \n")

t=turtle.Turtle()

t.color(pen_color)
t.fillcolor(fill_color)
angle=360/num_sides
t.begin_fill()
for i in range(num_sides):
    t.forward(side_len)
    t.right(angle)
t.end_fill()
    
    