from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_forwrd():
    timmy.forward(19)

screen.listen()
screen.onkey(move_forwrd,key="space")
screen.onkey(move_forwrd(),key="Up")

screen.exitonclick()



