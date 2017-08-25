import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor('blue')

    ralph = turtle.Turtle()
    ralph.color('pink')
    ralph.shape('turtle')

    draw_square(ralph)

    window.exitonclick()


draw_art()