import turtle

t = turtle.Pen()
t.speed(0)

turtle.bgcolor("white")

colors = ["red", "yellow", "green", "blue", "orange", "purple", "pink", "gray"]

# Ask the user for the number of sides without any upper limit (but it should be a positive integer)
sides = int(turtle.numinput("Number of sides", "How many sides do you want?", 4, 1))

for x in range(360):
    """
    In the statement for x in range(360):, the variable x will start from 0 and go up to,
    but not include, 360. So, the loop will iterate 360 times with x taking on values from 0 to 359 inclusive.

    Here's a breakdown:

    First iteration: x = 0
    Second iteration: x = 1
    Third iteration: x = 2
    ...
    359th iteration: x = 358
    360th (and last) iteration: x = 359
    
    The range() function, when given a single argument like range(360), assumes a starting value of 0
    and increments by 1 until it reaches the specified value (in this case, 360), but it doesn't include the ending value.
    """

    t.pencolor(colors[x % len(colors)])
    """
    Use modulo (returns the remainder of a division operation)
    with the length of the colors list to cycle through colors
    
    For example:
    7 % 3 would return 1, because when 7 is divided by 3, the remainder is 1.
    10 % 2 would return 0, because 10 is divisible by 2 with no remainder.

    len() returns the number of items in that object
    """

    t.forward(x * 3 / sides + x)
    """
    This line determines how far the turtle moves forward in each iteration of the loop.

    x * 3 / sides: Here, x is multiplied by 3 and then divided by the number of sides.
    As x increases with each iteration, the distance the turtle moves forward will also increase.
    The division by sides ensures that the movement is scaled based on the number of sides;
    for a larger number of sides, the turtle will move shorter distances, and vice versa.

    + x: This adds an additional increment based on the current iteration number.
    This means that as the loop progresses, the turtle will move forward by increasingly larger steps.

    Mathematically, the forward movement is given by the formula: distance = ((x * 3) / sides) + x
    """

    t.left(360 / sides + 1)
    """"
    This line determines the angle by which the turtle turns left in each iteration.

    360 / sides: This ensures that the turtle turns by an angle that would complete
    a full circle (360 degrees) after drawing the specified number of sides.
    For instance, for a square (4 sides), the turtle would turn by 90 degrees in each iteration.

    + 1: This adds an extra degree to the turn, making the pattern more intricate
    and ensuring that it doesn't just draw regular polygons.

    Mathematically, the turn angle is given by the formula: angle = (360 / sides) + 1
    """

    t.width(x * sides / 200)
    """
    This line determines the width of the line the turtle draws.

    x * sides: This multiplies the current iteration number x with the number of sides,
    making the width increase as the loop progresses and also scaling it based on the number of sides.

    / 200: This division scales down the width to ensure it doesn't become too large.
    The value 200 is somewhat arbitrary and can be adjusted to achieve different visual effects.

    Mathematically, the line width is given by the formula: width = (x * sides) / 2
    """

    #These formulas together create a dynamic and visually appealing pattern,
    #with the turtle's movement, turn angle, and line width all changing as the loop progresses.

turtle.done()
