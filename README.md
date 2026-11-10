Frosty the Snowman: Turtle Graphics Scene
CMPSC 8, Project 1
Authors: Ethan K, Melissa S
 
A Python program that uses the turtle module to draw a winter scene: a snowman wearing a hat and scarf, a pine tree, a sun, a blue sky, and snow on the ground. The scene is built entirely from three basic shapes (circles, triangles, and rectangles), which are combined by higher-level functions into the snowman, tree, and sun.
 
 
RUNNING THE PROGRAM
 
Requirements: Python 3 with the turtle module (included in the standard library).
 
python frosty.py
 
Replace frosty.py with whatever you (dear reader) named the file on download. A 600 x 600 window opens and the scene is drawn. Close the window to end the program.
 
 
WHAT GETS DRAWN
 
Sky: Light blue
Snow on the ground: White
Sun: Yellow
Tree leaves: Green
Tree trunk: Brown
Snowman body: White
Snowman arms: Brown
Snowman hat, eyes, buttons: Black
Snowman scarf: Red
Snowman nose: Orange
 
 
HOW THE CODE IS ORGANIZED
 
The main program only calls three functions: draw_background(), draw_frosty(), and finish(). Everything else is built from custom functions in three layers.
 
Shape functions (the only functions that draw filled shapes):
- draw_circle(color, x, y, r)
- draw_triangle(color, x, y, base, a1, s1, a2, s2)
- draw_rectangle(color, x, y, base, height)
 
Feature functions (built from the shapes):
- draw_snow, draw_trunk, draw_leaves, draw_sun
- frosty_scarf, frosty_hat, frosty_buttons, frosty_eyes, frosty_nose
- frosty_line (draws the two arms as straight lines)
 
Higher-level functions (group the features into parts of the scene):
- draw_background, draw_tree
- draw_frosty, frosty_body, frosty_arms, frosty_decor, frosty_face
 
 
LOOPS
 
1. Tree leaves: draw_leaves draws three triangles, each smaller than the last and shifted up and over so they stay centered on the trunk.
2. Snowman body: frosty_body draws three circles, each smaller than the last and placed higher so they overlap slightly.
3. Buttons: frosty_buttons draws three identical buttons, moving up each time.
 
 
COORDINATES
 
The window is 600 x 600, and turtle's origin (0, 0) is the center. The x-values run from -300 (left) to 300 (right) and the y-values from -300 (bottom) to 300 (top). Every shape function takes an (x, y) position:
- Circles are positioned by their center.
- Rectangles and triangles are positioned by their starting (bottom-left) corner.
