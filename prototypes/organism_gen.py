from random import randint, choice
from tkinter import *
from turtle import RawTurtle, TurtleScreen
from EvoSim.organism import Organism, random_organism

# Primary Colours Array for testing
prim_colours = ["red", "blue", "yellow"]


# Function to create a new organism and display its basic attributes
# Also calls the function that displays the organisms
def add_organisms(turtle, canvas, screen, canvas_x, canvas_y, nam_label, pop_label, button):
    button.config(state="disabled")
    rand_org = random_organism()
    nam_label.config(text="Name: " + rand_org.genus + " " + rand_org.species)
    pop_label.config(text="Population: " + str(rand_org.population))

    screen.tracer(0)
    draw_circle(turtle, canvas, screen, canvas_x, canvas_y, rand_org.population)
    canvas.update()
    button.config(state="normal")


# Function to draw circles of a random colour on the canvas
# Number of circles drawn is determined by organism's population
def draw_circle(turtle, canvas, screen, canvas_x, canvas_y, rand_pop):

    # This statement modifies the color to be a normal string as this is what turtle expects
    turtle.color(str(["#"+''.join([choice('ABCDEF0123456789') for i in range(6)])]).replace("'", "").replace('[', '').replace(']', ''))

    for i in range(0, int(rand_pop/500)):
        turtle.penup()
        turtle.setx(randint(canvas_x*-1, canvas_x))
        turtle.sety(randint(canvas_y*-1, canvas_y))

        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(30)
        turtle.end_fill()


def run():

    # Root Tkinter window
    root = Tk()
    root.winfo_toplevel().iconphoto(True, Image("photo", file="../EvoSim/assets/icon.png"))
    root.title("EvoSim - Organism Generation")
    root.winfo_toplevel().geometry("600x500")

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
    population_label = Label(root, text="Population: None")
    population_label.pack()

    # Button to generate circles at random positions
    gen_button = Button(root, text="Generate", command=lambda: add_organisms(turtle, canvas, screen, x, y, name_label, population_label, gen_button))
    gen_button.pack()

    #screen.update()
    # Keeps the screen visible
    screen.mainloop()


if __name__ == "__main__":
    run()
