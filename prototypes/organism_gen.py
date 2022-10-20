import turtle


def draw_circle(x, y):
    turtle.penup()
    turtle.setx(x)
    turtle.sety(y)

    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()


window = turtle.Screen()
turtle.speed(0)
turtle.pensize(5)
turtle.hideturtle()

# Ensures instant drawing
turtle.tracer(0)

# Circle Outline
turtle.color("black")
turtle.fillcolor("black")


draw_circle(0, 0)
# draw_circle(turtle.window_width(), turtle.window_height())
print(turtle.window_width())
draw_circle(930, 0)

# Ensures instant drawing
turtle.update()
turtle.mainloop()
