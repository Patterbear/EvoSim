from random import randint, choice
from tkinter import *
from turtle import RawTurtle, TurtleScreen
from EvoSim.environment import Environment, generate_terrain_types

env_types = ['grass', 'water', 'sand', 'rock']


def new_env(t, c, s):
    print("NEW ENV")
    env = Environment()
    generate_terrain_types()

    env.test_grid_fill()
    env.print_grid()

    draw_env(t, c, s, env)


def draw_env(t, c, s, env_to_draw):
    for i in range(0, len(env_to_draw.grid) - 1):
        for j in range(0, len(env_to_draw.grid[i])):
            s.tracer(0)
            t.speed(0)
            draw_tile(t, c, s, i, j, env_to_draw.grid[i][j])
            s.update()


def draw_tile(t, c, s, x, y, terrain_type):
    t.penup()
    t.setx(x)
    t.sety(y)

    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.forward(10)  # Forward turtle by s units
        t.left(90)  # Turn turtle by 90 degree
    t.end_fill()






def run():
    # Root Tkinter window
    root = Tk()
    root.winfo_toplevel().iconphoto(True, Image("photo", file="../EvoSim/assets/icon.png"))
    root.title("EvoSim - Environment Generation")
    root.winfo_toplevel().geometry("1280x720")

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

    # Labels to display generated organism attributes
    name_label = Label(root, text="Name: None")
    name_label.pack()

    # Button to generate circles at random positions
    Button(root, text="Generate", command=lambda: new_env(turtle, canvas, screen)).pack()

    # Keeps the screen visible
    screen.mainloop()


if __name__ == "__main__":
    run()
