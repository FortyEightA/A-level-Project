import pyglet
import math
from pyglet.window import key
from pyglet import clock


# initialise the background and player_image as soon as the window is drawn
resx, resy = 860, 540
backgroundimage = pyglet.image.load('whitebackground.jpg')
player_image = pyglet.image.load('testsprite.png',)
player_image.anchor_x = player_image.width//2
player_image.anchor_y = player_image.height//2
player = pyglet.sprite.Sprite(player_image, x=resx//2, y=resy//2)

# create boolean variables for the buttons to allow repeat actions
w, a, s, d = False, False, False, False

# player speed
speed = 5


class main(pyglet.window.Window):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_draw(self):
   
        # drawing background and sprites
        backgroundimage.blit(0, 0)
        player.draw()

    def on_key_press(self, symbol, modifiers):
        # esc to exit
        if symbol == key.ESCAPE:
            self.close()

        # initialise global variables into local scope
        global w, a, s, d

        # look for key press
        if symbol == key.W:
            w = True
        elif symbol == key.A:
            a = True
        elif symbol == key.S:
            s = True
        elif symbol == key.D:
            d = True

    def on_key_release(self, symbol, modifiers):
    
        # initialise global variables into local scope
        global w, a, s, d

        # look for key release
        if symbol == key.W:
            w = False
        elif symbol == key.A:
            a = False
        elif symbol == key.S:
            s = False
        elif symbol == key.D:
            d = False

    # function to move the player sprite
    def moveT(dt):
        if w == True:
            player.y += 5
        elif s == True:
            player.y -= 5
        # if a == True:
        #     player.x -= 5
        # elif d == True:
        #     player.x += 5

    def rotateT(dt):
        if a == True:
            player.rotation -= 5
        if d == True:
            player.rotation += 5

    
    pyglet.clock.schedule_interval(moveT, 1/60)
    pyglet.clock.schedule_interval(rotateT, 1/60)


if __name__ == '__main__':
    
    # variables for the screen size

    # create window object
    mainwindow = main(resx, resy,
                      resizable=False,
                      style=pyglet.window.Window.WINDOW_STYLE_DEFAULT,)

    # run program(will replace with black magic fkery once i found out how to do it
    # https://stackoverflow.com/questions/41924002/how-do-i-run-the-pyglet-window-clear-function-through-a-on-button-press-event)
    pyglet.app.run()
