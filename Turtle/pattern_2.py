def Turtle_2():
    """Gives a torch reflection type pattern"""
    import turtle, math
    roc = turtle.Turtle()
    roc.speed(0)
    roc.hideturtle()
    roc.getscreen().bgcolor("black")
    colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
    roc.color("white")
    i = 10

    while i <= 100:
        roc.penup()
        roc.forward(i)
        roc.pendown()
        roc.circle(i)
        roc.penup()
        roc.backward(i)
        roc.pendown()
        i += 5
    input()

