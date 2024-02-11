import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Circle Drawing")

# Create a turtle object
circle_drawer = turtle.Turtle()
circle_drawer.speed(10)  # Set drawing speed to slowest

# Set the turtle shape
circle_drawer.shape("turtle")

# Draw a circle with a specified radius
circle_drawer.circle(20)

# Close the turtle graphics window
turtle.done()
