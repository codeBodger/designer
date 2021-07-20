from designer import *

set_window_color((colors['lavender']))
#face = make_circle((400, 300), 100, colors['lightyellow'])
face = circle(100, colors['lightyellow'], 400, 300)
# move_left(face)
# left = make_circle((450, 275), 20, colors['black'])
left = circle(20, colors['black'], 450, 275)
# right = make_circle((350, 275), 20, colors['black'])
right = circle(20, colors['black'], 350, 275)
# smile = make_arc(525, 500, 350, 275, colors['pink'], math.pi, 0, 3)

smiley_face = group(face, right, left)
#move_left(smiley_face)
rotate(smiley_face, 270, 1)
make_text('green', "Hello", 30, 0, 0)
make_text('purple', 'World', 30, 550, 550)
image('https://st4.depositphotos.com/18504396/39462/i/1600/depositphotos_394625900-stock-photo-cup-drink-rustic-wooden-background.jpg', 100, 100, 100, 100)
# image('API_design/images/duck.png', 100, 100, 100, 100)
# make_image('images/crab.png', 500, 500, 50, 50)
#rotate(face, 125, 360)
# rotate(smiley_face, direction=125, angle_limit=360)
draw()