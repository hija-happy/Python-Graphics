# Program to draw a circle and a sqaure and to fill colors
import turtle

# To create a turtle object shape 1 sqaure
square = turtle.Turtle()

# To fill color to specifies color
square.fillcolor("Red")

# Begin filling with the specified color
square.begin_fill()

# Move the turtle to the starting position for the square
square.penup()
square.goto(0, 0)
square.pendown()


# Move the turtle forward and turn right four times to draw a square
for _ in range(4):
    square.backward(100)
    square.right(90)

# End filling with the specified color
square.end_fill()

# To create a turtle object shape 2 circle
_circle = turtle.Turtle()

# To fill color to specifies color
_circle.fillcolor("Green")

# Move the turtle to the starting position for the circle
_circle.penup()
_circle.goto(100,100)
_circle.pendown()

# Begin filling with the specified color
_circle.begin_fill()

#Draaw a circle
_circle.circle(50)

# End filling with the specified color
_circle.end_fill()

# Close the turtle graphics window
turtle.done()


