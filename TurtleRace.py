import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Vertical Turtle Race with Timer and Power-ups")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)

# Ask user for the number of turtles (up to 20)
num_turtles = screen.numinput("Turtle Race", "How many turtles do you want to race? (2-20)", minval=2, maxval=20)
if not num_turtles:
    num_turtles = 3  # Default to 3 turtles if no input

num_turtles = int(num_turtles)

# Set up the race track
track_height = 400
start_line = -track_height / 2  # Start at the bottom of the screen
finish_line = track_height / 2  # Finish at the top of the screen

# Create turtles with valid colors
valid_colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "violet", "cyan",
                "lime", "indigo", "magenta", "gray", "turquoise", "black", "white", "beige", "navy", "teal"]
turtles = []

# Create the turtle objects
spacing = 40  # Space between turtles on the x-axis
x_start = -((spacing * (num_turtles - 1)) / 2)  # Start in the center of the screen

for i in range(num_turtles):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(valid_colors[i % len(valid_colors)])  # Cycle through the valid colors if more than available colors
    t.penup()
    t.goto(x_start + i * spacing, start_line)  # Position turtles centered horizontally
    t.setheading(90)  # Face the turtles upwards (towards the finish line)
    turtles.append(t)

# Create a timer
timer = 30  # Time in seconds
timer_display = turtle.Turtle()
timer_display.hideturtle()
timer_display.penup()
timer_display.goto(0, 150)
timer_display.write(f"Time: {timer}s", align="center", font=("Arial", 16, "bold"))

# Display the winner at the end
winner_display = turtle.Turtle()
winner_display.hideturtle()
winner_display.penup()
winner_display.goto(0, -200)

# Add obstacles and power-ups
obstacles = [random.randint(-250, 250) for _ in range(3)]  # Random x positions for obstacles
powerups = [random.randint(-250, 250) for _ in range(2)]  # Random x positions for power-ups


# Function to move turtles with random distances
def move_turtle(t):
    distance = random.randint(1, 10)

    # Check if turtle hits an obstacle (it slows down)
    if t.xcor() in obstacles:
        distance -= random.randint(3, 5)

    # Check if turtle gets a power-up (it speeds up)
    if t.xcor() in powerups:
        distance += random.randint(5, 7)

    # Move the turtle upwards (along positive y-axis)
    t.sety(t.ycor() + distance)


# Draw the finish line
finish_line_turtle = turtle.Turtle()
finish_line_turtle.hideturtle()
finish_line_turtle.penup()
finish_line_turtle.goto(-400, finish_line)
finish_line_turtle.pendown()
finish_line_turtle.forward(800)
finish_line_turtle.penup()

# Start the race
race_in_progress = True
start_time = time.time()

while race_in_progress:
    # Countdown Timer
    elapsed_time = int(time.time() - start_time)
    remaining_time = timer - elapsed_time
    timer_display.clear()
    timer_display.write(f"Time: {remaining_time}s", align="center", font=("Arial", 16, "bold"))

    # Move each turtle
    for t in turtles:
        move_turtle(t)

        # Check if any turtle crosses the finish line
        if t.ycor() >= finish_line:
            race_in_progress = False
            winner = t
            break

    # Stop race if time runs out
    if remaining_time <= 0:
        race_in_progress = False
        winner = None
        break

# Display the winner
if winner:
    winner_display.clear()
    winner_display.write(f"The winner is the {winner.color()[0]} turtle!", align="center", font=("Arial", 16, "bold"))
else:
    winner_display.clear()
    winner_display.write("Time's up! No winner.", align="center", font=("Arial", 16, "bold"))

turtle.done()
