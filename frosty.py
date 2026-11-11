import turtle

frosty = turtle.Turtle()
screen = turtle.Screen()

width = 600
height = 600
speed = 6

frosty.speed(speed)

screen.setup(width, height)

def draw_background(color): 
    """
    Description: Sets the window's background to the given color for sky, then makes 
    the rest of the scene by calling draw_snow, draw_tree, and draw_sun.

    Parameters:
        color (string): the color for the sky

    Return values: None (calls the other three functions and sets the sky color)
    """

    screen.bgcolor(color)
    draw_snow("white", -300, -300, 600, 200)
    draw_tree()
    draw_sun("yellow", 125, 215, 40)

def draw_snow(color, x, y, base, height):
    """
    Description: Draws the snow on the ground as one wide white rectangle at 
    the bottom third of the window by calling draw_rectangle.

    Parameters: 
        color (string): sets the color for the snow
        x, y (int): the bottom left corner of the ground
        base (int): the width of the ground
        height (int): the height of the ground

    Return values: None (draws the ground on the screen)
    """

    draw_rectangle(color, x, y, base, height)

def draw_tree(): 
    """
    Description: Draws the whole tree by calling draw_trunk and then draw_leaves, 
    and the leaves sit on top of the trunk.

    Parameters: 
        None. The colors, position, and sizes are set inside this 
        function and passed to the functions it calls.

    Return values: None (calls the other functions to draw the tree on screen)
    """

    draw_trunk("brown", 185, -155, 30, 85)
    draw_leaves("green", 135, -80, 130, 120)

def draw_trunk(color, x, y, base, height):
    """
    Description: Draws the tree trunk as one rectangle by calling draw_rectangle.

    Parameters: 
        color (string): the color of the tree trunk (brown)
        x, y (int): the bottom left corner of the trunk
        base (int): the width of the trunk
        height (int): the height of the trunk

    Return values: None (draws the trunk on screen)
    """

    draw_rectangle(color, x, y, base, height) 

def draw_leaves(color, x, y, base, angle):
    """
    Description: Draws the tree's leaves as three green triangles 
    stacked on top of each other, each one smaller than the one 
    below it. A loop calls draw_triangle three times, and 
    each pass moves the starting point up and over and 
    shrinks the triangle so the layers stay centered 
    over the trunk.

    Parameters: 
        color (string): the color of the leaves (green)
        x, y (int): the bottom left corner of the lowest triangle
        base (int): the side length of the lowest triangle
        angle (int): the angle in degrees to turn left at each corner of a triangle

    Return values: None (draws the leaves on screen)
    """

    side = base
    axis_x = x
    axis_y = y

    for _ in range(3):
        draw_triangle(color, axis_x, axis_y, side, angle, side, angle, side)
        axis_y += 45
        axis_x += 12.5
        side -= 25

def draw_sun(color, x, y, r):
    """
    Description: Draws the sun as a filled circle in the upper right
    of the sky by calling draw_circle

    Parameters: 
        color (string): the color of the sun (yellow)
        x, y (int): the center of the sun
        r (int): the radius of the sun

    Return values: None (draws the sun on the screen)
    """

    draw_circle(color, x, y, r)

def draw_frosty():
    """
    Description: Draws the whole snowman. It calls frosty_body, which draws the 
    three circles and then the arms and accessories, and then calls frosty_face 
    so the eyes and nose are drawn on top of the head.

    Parameters: 
        None. Everything is set inside this function and passed to the functions it calls.

    Return values: None (draws the snowman on the screen)
    """

    frosty_body("white", -120, -120, 85)
    frosty_face()

def frosty_body(color, x, y, r):
    """
    Description: Draws the three white circles of the snowman (bottom, torso, and head) using a 
    loop that calls draw_circle three times. Each circle is smaller than the one below it 
    and is placed higher so they stack and overlap slightly. After the loop, it works out 
    the center and radius of the torso and passes them to frosty_arms, 
    then calls frosty_decor to draw the accessories.

    Parameters: 
        color (string): the color of the body (white)
        x, y (int): the center of the bottom circle. 
        All three circles share the same x-value
        r (int): the radius of the bottom circle

    Return values: None (draws the body, arms, and accessories on the screen)
    """
    
    radius = r
    axis_y = y

    for _ in range(3):
        draw_circle(color, x, axis_y, radius)
        axis_y += radius + (radius - 12) - 20
        radius -= 12

    torso_r = r - 12
    torso_y = y + r + torso_r - 20

    frosty_arms("brown", x, torso_y, torso_r, 130)
    frosty_decor()

def frosty_arms(color, x, y, r, length):
    """
    Description: Draws the snowman's two arms by calling the frosty_line function, 
    which draws one arm on each side of the torso.

    Parameters: 
        color (string): the color of the arms (brown)
        x, y (int): the center of the torso (the middle circle of the body)
        r (int): the radius of the torso circle, so the arms start at its 
        left and right edges 
        length (int): the length value of each arm

    Return values: None (draws the arms on the screen)
    """

    frosty_line(color, x, y, r, length)

def frosty_decor():
    """
    Description: Groups the snowman's accessories by calling frosty_scarf, 
    frosty_hat, and frosty_buttons

    Parameters: 
        None. Everything is set inside this function and passed to the 
        functions it calls

    Return values: None (draws the accessories on the screen)
    """

    frosty_scarf("red", -155, 68, 70, 16)
    frosty_hat("black", -182, 182, 124, 15) 
    frosty_buttons("black", -120, -20, 9)

def frosty_face():
    """
    Description: Draws the snowman's face by calling frosty_eyes and frosty_nose

    Parameters: 
        None. Everything is set inside this function and passed to the 
        functions it calls

    Return values: None (draws the face on the screen)
    """

    frosty_eyes("black", -120, 140, 9)
    frosty_nose("orange", -120, 103, 90, 165, 93, 105, 24)

def frosty_line(color, x, y, r, length):
    """
    Description: Draws both arms as thick (size 5) straight lines that mirror each other. 
    The pen size is set back to 1 after it finishes. The right arm starts at the right
    edge of the torso and points up and to the right. The left arm starts at the left
    edge of the torso and points up and to the left.

    Parameters: 
        color (string): the color of the lines (brown)
        x, y (int): the center of the torso circle
        r (int): the radius of the torso circle
        length (int): the length of each line

    Return values: None (draws the two lines on the screen)
    """

    frosty.pencolor(color)
    frosty.penup()
    frosty.goto(x + r, y) 
    frosty.setheading(65)
    frosty.pensize(5)
    frosty.pendown()
    frosty.forward(length)
    frosty.penup()
    frosty.goto((x - r), y)
    frosty.setheading(115)
    frosty.pendown()
    frosty.forward(length)
    frosty.pensize(1)

def frosty_scarf(color, x, y, base, height):
    """
    Description: Draws the scarf as one rectangle between the head and the torso 
    by calling draw_rectangle

    Parameters: 
        color (string): the color of the scarf (red)
        x, y (int): the bottom left corner of the scarf
        base (int), height (int): the width and height of the scarf

    Return values: None (draws the scarf on the screen)
    """

    draw_rectangle(color, x, y, base, height)

def frosty_hat(color, x, y, base, height): 
    """
    Description: Draws the hat from two rectangles by calling 
    draw_rectangle twice: a wide, short brim, and a narrower,
    taller top part centered on the brim.

    Parameters:
        color (string): the color of the hat (black)
        x, y (int): the bottom left corner of the brim, resting on top of the head
        base (int), height (int): the width and height of the brim. 
        The size and position of the top part are calculated from these

    Return values: None (draws the hat on the screen)
    """

    draw_rectangle(color, x, y, base, height)

    top_width = base * 0.55 
    top_x = x + (base - top_width) / 2
    draw_rectangle(color, top_x, y + height, top_width, height * 4)

def frosty_buttons(color, x, y, r):
    """
    Description: Draws three identical buttons in a vertical line on the torso, 
    using a loop that calls draw_circle three times. Each button is placed 
    above the one before it.

    Parameters: 
        color (string): the color of the buttons (black)
        x, y (int): the center of the bottom button. The other two are placed 
        above it
        r (int): the radius of each button

    Return values: None (draws the buttons on the screen)
    """

    for _ in range(3):
        draw_circle(color, x, y, r)
        y += 30

def frosty_eyes(color, x, y, r):
    """
    Description: Draws two identical eyes placed symmetrically on either 
    side of the point (x, y) by calling draw_circle twice

    Parameters: 
        color (string): the color of the eyes (black)
        x, y (int): the point midway between the two eyes, in the 
        upper part of the head
        r (int): the radius of each eye
    
    Return values: None (draws the eyes on the screen)
    """

    draw_circle(color, x + 25, y, r)
    draw_circle(color, x - 25, y, r)

def frosty_nose(color, x, y, base, a1, s1, a2, s2):
    """
    Description: Draws the carrot nose as a thin triangle that starts just
    below the eyes, on the head's center line, and points outward, by calling
    draw_triangle

    Parameters: 
        color (string): the color of the nose (orange)
        x, y (int): the starting corner of the nose, just below the eyes
        on the head's center line
        base (int): the length of the first side
        a1, s1 (int): the angle in degrees to turn left after the first side, 
        and the length of the second side
        a2, s2 (int): the angle in degrees to turn left after the second side, 
        and the length of the third side

    Return values: None (draws the nose on the screen)
    """
    
    draw_triangle(color, x, y, base, a1, s1, a2, s2)

def draw_triangle(color, x, y, base, a1, s1, a2, s2):
    """
    Description: Helper function that draws one filled triangle. It moves 
    to (x, y) with the pen up, sets the heading (angle to east) 0, puts
    the pen down, sets the pen and fill colors, and starts the fill. It 
    then draws the first side, turns left by a1, draws the second side,
    turns left by a2, and then draws the third side, and ends 
    the fill. It is used by draw_leaves and frosty_nose.

    Parameters: 
        color (string): the fill color
        x, y (int): the starting corner of the triangle
        base (int): the length of the first side, drawn horizontally
        a1 (int): the angle in degrees to turn after the first side
        s1 (int): the length of the second side
        a2 (int): the angle in degrees to turn after the second side
        s2 (int): the length of the third side, which closes the triangle

    Return values: None (draws the filled triangle on the screen)
    """
    frosty.penup()
    frosty.goto(x, y)
    frosty.setheading(0)
    frosty.pendown()
    frosty.pencolor("Black")
    frosty.fillcolor(color)
    frosty.begin_fill()
    frosty.forward(base)
    frosty.left(a1) 
    frosty.forward(s1)
    frosty.left(a2) 
    frosty.forward(s2)
    frosty.end_fill()

def draw_circle(color, x, y, r):
    """
    Description: Helper function that draws one filled circle centered on (x, y). 
    Turtle draws a circle starting from its bottom point, so the function moves 
    to (x, y - r) first, which puts the center of the circle at (x, y). It is 
    used by draw_sun, frosty_body, frosty_buttons, and frosty_eyes.

    Parameters: 
        color (string): the fill color
        x, y (int): the center of the circle
        r (int): the radius of the circle

    Return values: None (draws the filled circle on the screen)
    """

    frosty.penup()
    frosty.goto(x, y - r)
    frosty.setheading(0)
    frosty.pendown()
    frosty.pencolor("Black")
    frosty.fillcolor(color)
    frosty.begin_fill()
    frosty.circle(r)
    frosty.end_fill()

def draw_rectangle(color, x, y, base, height):
    """
    Description: Helper function that draws one filled rectangle with its 
    bottom left corner at (x, y). It sets the heading to 0 first so that 
    the rectangle is always drawn the same way, then draws the four 
    sides inside a fill. It is used by draw_snow, draw_trunk, 
    frosty_scarf, and frosty_hat.

    Parameters:
        color (string): the fill color
        x, y (int): the bottom left corner of the rectangle
        base (int): the width of the rectangle
        height (int): the height of the rectangle

    Return values: None (draws the filled rectangle on the screen)
    """

    frosty.penup()
    frosty.goto(x, y)
    frosty.setheading(0)
    frosty.pendown()
    frosty.pencolor("Black")
    frosty.fillcolor(color)
    frosty.begin_fill()
    for _ in range(2):
        frosty.forward(base)
        frosty.left(90)
        frosty.forward(height)
        frosty.left(90)
    frosty.end_fill()

def finish():
    """
    Description: Keeps the window open until the user closes it
    and hides turtle object.

    Parameters:
        None.

    Return values: None (keeps the drawing on the screen)
    """

    frosty.hideturtle()
    turtle.done()


if __name__ == "__main__":
    draw_background("light blue")
    draw_frosty()
    finish()
