from turtle import  Turtle , Screen
tim = Turtle()

screen = Screen()

def forward():
    tim.forward(10)
def backward():
    tim.backward(10)

def turn_right():
    new_headind = tim.heading() - 10
    tim.setheading(new_headind)

def turn_left():
    new_headind = tim.heading() + 10
    tim.setheading(new_headind)

screen.listen()
screen.onkey(forward,key="Up")
screen.onkey(backward,key="Down")
screen.onkey(turn_right,key="Right")
screen.onkey(turn_left,key="Left")



screen.exitonclick()