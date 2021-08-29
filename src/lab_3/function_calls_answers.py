from designer import *

# set background color
set_window_color('lightgreen')

# make face
face = circle('lightyellow', 100, 400, 300)

# make eyes
right_eye = circle('black', 10, 450, 275)
left_eye = circle('black', 10, 350, 275)

# make eyebrows
right_eyebrow = line(2, 'black', 425, 265, 470, 250)
left_eyebrow = line(2, 'black', 375, 265, 330, 250)

# make mouth
mouth = circle('black', 20, 400, 350)

#EXTRA CREDIT, GROUPING
emoji = group(face, right_eye, left_eye, right_eyebrow, left_eyebrow, mouth)
glide_down(emoji, 1)


draw()
'''
How many function calls are there?
There are 4 function calls
 
 For each function call: 
 1. Explain what the function does (What is its purpose?) 
 2. Note any arguments and what the arguments represent  
 3. Identify the return value
 You should answer 1-3 for every function call, so however many you identified in the first question.  

set_window_color: 
 1. sets the background color of the window. 
 2. Takes 1 argument, the color to set the background
 3. Returns None
 
circle: 
1. Creates a circle to draw on the screen 
2. Takes 4 arguments: the first is the radius of the circle to be drawn as an int, then the color of the circle,
then the x position of the center of the circle on the window as an int, then the y position of the center of the
circle on the window as an int 
3. Returns the circle created

glide_left: 
1. Moves the given parameter to the left on the window
2. Takes 2 arguments, the object to be moved and the speed at which to move it 
3. Returns None

draw: 
1. Starts the window and all actions
2. Does not take any arguments
3. Returns None   


'''