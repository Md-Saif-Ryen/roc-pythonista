def Turtle5(angle, speed, color, bg_color):
    import turtle as roc
    colors = ["red", "blue", "cyan", "purple", "indigo"]
    roc.hideturtle()
    roc.getscreen().bgcolor(bg_color)
    roc.speed(speed)
    roc.color(color)
    i = 0
    while i < 300:
        roc.circle(i)
        j = 0
        while j < 4:
            roc.forward(100)
            roc.left(90)
            j += 1

        roc.left(angle)
        j = 0
        i += 1

    roc.exitonclick()

