from turtle import *

sides = int(input("Enter number of sides:"))
angle = 360/sides

length = int(input("Enter desired length:"))

print ("sides:", sides, "angle:", angle)

speed(1)

begin_fill()
fillcolor("red")

skips = sides
for lines in range(sides):
    forward(length)
    right(angle)

end_fill()

exitonclick()
