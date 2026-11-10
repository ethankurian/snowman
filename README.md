Frosty the Snowman: Turtle Graphics Scene

CMPSC 8, Project 1

Authors: Ethan K, Melissa S

A Python program that uses the turtle module to draw a winter scene: a snowman wearing a hat and scarf, a pine tree, a sun, a blue sky, and snow on the ground. The scene is built entirely from three basic shapes (circles, triangles, and rectangles), which are combined by higher-level functions into the snowman, tree, and sun.

Running the program

Requirements: Python 3 with the turtle module (including the standard library).

python frosty.py

Replace frosty.py with whatever you (dear reader) named the file on download. A 600 x 600 window opens and the scene is drawn. Close the window to end the program.

What gets drawn
Element	Color
Sky	Light blue
Snow on the ground	White
Sun	Yellow
Tree leaves Green
Tree trunk Brown
Snowman body White
Snowman arms Brown
Snowman hat, eyes, buttons	Black
Snowman scarf Red
Snowman nose Orange
How the code is organized

The main program only calls two functions, draw_background(), draw_frosty(), and finish(). Everything else is built from custom functions in three layers.

Shape functions (the only functions that draw filled shapes):

draw_circle(color, x, y, r)
draw_triangle(color, x, y, base, a1, s1, a2, s2)
draw_rectangle(color, x, y, base, height)

Feature functions (built from the shapes):

draw_snow, draw_trunk, draw_leaves, draw_sun
frosty_scarf, frosty_hat, frosty_buttons, frosty_eyes, frosty_nose
frosty_line (draws the two arms as straight lines)

Higher-level functions (group the features into parts of the scene):

draw_background(color)
├── draw_snow ............ draw_rectangle
├── draw_tree
│   ├── draw_trunk ....... draw_rectangle
│   └── draw_leaves ...... draw_triangle (loop, 3 times)
└── draw_sun ............. draw_circle

draw_frosty()
├── frosty_body
│   ├── draw_circle (loop, 3 times: bottom, torso, head)
│   ├── frosty_arms ...... frosty_line
│   └── frosty_decor
│       ├── frosty_scarf .. draw_rectangle
│       ├── frosty_hat .... draw_rectangle (twice: brim and top)
│       └── frosty_buttons  draw_circle (loop, 3 times)
└── frosty_face
    ├── frosty_eyes ...... draw_circle (twice)
    └── frosty_nose ...... draw_triangle
Loops
Tree leaves: draw_leaves draws three triangles, each smaller than the last and shifted up and over so they stay centered on the trunk.
Snowman body: frosty_body draws three circles, each smaller than the last and placed higher so they overlap slightly.
Buttons: frosty_buttons draws three identical buttons, moving up each time.

Coordinates
The window is 600 x 600, and turtle's origin (0, 0) is the center. The x-values run from -300 (left) to 300 (right) and the y-values from -300 (bottom) to 300 (top). 
Every shape function takes an (x, y) position:
circles are positioned by their center
rectangles and triangles are positioned by their starting (bottom-left) corner