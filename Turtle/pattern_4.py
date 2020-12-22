def Turtle4():
    """gives a pattern of star with a bit of 3d effect"""
    import turtle
    roc = turtle.Turtle()
    roc.speed(0)
    roc.hideturtle()
    roc.getscreen().bgcolor("black")
    roc.color("silver")
    for i in range(1000):
        i += 100
        roc.forward(i)
        # roc.circle(i)
        roc.left(168.5)

