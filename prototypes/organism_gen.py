from random import randint
from tkinter import *
from turtle import RawTurtle, TurtleScreen

# Primary Colours Array for testing
prim_colours = ["red", "blue", "yellow"]


# Function to draw circles of a random colour on the canvas
def draw_circle(x, y):
    turtle.color(prim_colours[randint(0, 2)])

    turtle.penup()
    turtle.setx(x)
    turtle.sety(y)

    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()


# Root Tkinter window
root = Tk()
root.winfo_toplevel().iconphoto(True, Image("photo", file="../EvoSim/assets/icon.png"))
root.title("EvoSim - Organism Generation")
root.winfo_toplevel().geometry("600x450")

# Canvas to host the Turtle canvas
canvas = Canvas(root, width=400, height=400)
canvas.pack()
screen = TurtleScreen(canvas)
turtle = RawTurtle(canvas)

# Turtle configurations
turtle.speed(0)
turtle.pensize(5)
turtle.hideturtle()

# Assigning canvas dimensions to variables and creating limits
x = canvas.winfo_width() - 200
y = canvas.winfo_height() - 200

# Button to generate circles at random positions
Button(root, text="Test", command=lambda: draw_circle(randint(x*-1, x), randint(y*-1, y))).pack()

# Keeps the screen visible
screen.mainloop()
