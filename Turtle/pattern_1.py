def turtle_1():
    """Gives a 3d like pattern"""
    import turtle, math
    roc = turtle.Turtle()
    roc.speed(1000)
    roc.hideturtle()
    roc.getscreen().bgcolor("black")
    colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
    roc.color("silver")
    i = 1
    while i <= 300:
        roc.circle(i)
        roc.penup()
        roc.forward(i)
        roc.pendown()
        roc.left(45)
        roc.penup()
        roc.forward(i)
        roc.pendown()
        i += 1

    input()

