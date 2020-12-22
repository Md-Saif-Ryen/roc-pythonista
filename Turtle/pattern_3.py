def Turtle_3():
    """Gives spiral pattern made with two circles"""
    import math, turtle
    roc = turtle.Turtle()
    roc.speed(0)
    roc.hideturtle()
    roc.getscreen().bgcolor("black")
    roc.color("silver")
    i = 10
    while i <= 100:
        roc.forward(i)
        roc.circle(i * math.tan(89))
        roc.left(168.5)
        i += 1
    input()

