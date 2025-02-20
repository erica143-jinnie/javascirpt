import turtle
turtle.screen().bgcolor("Aqua")
turtle.screen().setup(300,400)
rectriangle = turtle.Turtle()

num_side = 4
side_length = 70
angle = 360.0 / num_side

for i in range(num_side):
    rec.forward(side_length)
    polygon.right(angle)

turtle.done()