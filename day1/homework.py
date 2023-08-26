from turtle import *

#we want print a house

#step 1:  draw a square
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of sqveare

#drawing a door

forward(70)
color("yellow")
left(90)
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(170, 170)
pendown()
color("blue")
right(60)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)

penup()
goto(50, 140)
pendown()
color("black")
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)





exitonclick()