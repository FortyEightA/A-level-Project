

import pyglet
from pyglet.window import key
from pyglet import clock


# initialise the background and player_image as soon as the window is drawn
resx, resy = 860, 540
backgroundimage = pyglet.image.load('images/whitebackground.jpg')

acceleration = 0.2
friction = 0.92

velX = 0
velY = 0
player_image = pyglet.image.load('images/testsprite.png',)
player_image.anchor_x = player_image.width//2
player_image.anchor_y = player_image.height//2
player = pyglet.sprite.Sprite(player_image, x=resx//2, y=resy//2)

# create boolean variables for the buttons to allow repeat actions
w, a, s, d = False, False, False, False
space = False
# player speed
max_speed = 7


def check_bounds(self):
    min_x = -self.image.width / 2
    min_y = -self.image.height / 2
    max_x = resx + self.image.width / 2
    max_y = resy + self.image.height / 2
    if self.x < min_x:
        self.x = max_x
    elif self.x > max_x:
        self.x = min_x
    if self.y < min_y:
        self.y = max_y
    elif self.y > max_y:
        self.y = min_y


class main(pyglet.window.Window):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_draw(self):
        # drawing background and sprites
        backgroundimage.blit(0, 0)
        player.draw()
        # player.draw()

    def on_key_press(self, symbol, modifiers):
        # esc to exit
        if symbol == key.ESCAPE:
            self.close()

        # initialise global variables into local scope
        global w, a, s, d, space

        # look for key press
        if symbol == key.W:
            w = True
            player.rotation = 0
        elif symbol == key.A:
            a = True
            player.rotation = 270
        elif symbol == key.S:
            s = True
            player.rotation = 180
        elif symbol == key.D:
            d = True
            player.rotation = 90
        elif symbol == key.SPACE:
            space = True

    def on_key_release(self, symbol, modifiers):

        # initialise global variables into local scope
        global w, a, s, d, space

        # look for key release
        if symbol == key.W:
            w = False
        elif symbol == key.A:
            a = False
        elif symbol == key.S:
            s = False
        elif symbol == key.D:
            d = False
        elif symbol == key.SPACE:
            space = False

    def update(dt):
        global velX, velY, acceleration, friction, space, w, a, s, d
        if space == True:

            if w == True:
                if a == True:
                    velX -= 3.5355
                    velY += 3.5355
                elif d == True:
                    velX += 3.5355
                    velY += 3.5355
                else:
                    velY += 5
            elif s == True:
                if a == True:
                    velX -= 3.5355
                    velY -= 3.5355
                elif d == True:
                    velX += 3.5355
                    velY -= 3.5355
                else:
                    velY -= 5
            elif a == True:
                velX -= 5

            elif d == True:
                velX += 5

        if a == True:
            if velX > -max_speed:
                velX -= acceleration
        if d == True:
            if velX < max_speed:
                velX += acceleration
        if w == True:
            if velY > -max_speed:
                velY += acceleration
        if s == True:
            if velY < max_speed:
                velY -= acceleration
        player.x += velX
        player.y += velY
        velX *= friction
        velY *= friction
        check_bounds(player)

    # function to move the player sprite

    # def moveT(dt):

    #     if w == True and d == True:
    #         player.y += 3.535533906
    #         player.x += 3.535533906
    #     elif w == True and a == True:
    #         player.y += 3.535533906
    #         player.x -= 3.535533906
    #     elif s == True and d == True:
    #         player.y -= 3.535533906
    #         player.x += 3.535533906
    #     elif s == True and a == True:
    #         player.y -= 3.535533906
    #         player.x -= 3.535533906
    #     elif w == True:
    #         player.y += speed
    #         player.rotation = 0
    #     elif s == True:
    #         player.y -= speed
    #         player.rotation = 180
    #     elif a == True:
    #         player.x -= speed
    #         player.rotation = 270
    #     elif d == True:
    #         player.x += speed
    #         player.rotation = 90

    pyglet.clock.schedule_interval(update, 1/60)


if __name__ == '__main__':

    # variables for the screen size

    # create window object
    mainwindow = main(resx, resy,
                      resizable=False,
                      style=pyglet.window.Window.WINDOW_STYLE_DEFAULT,)

    # run program(will replace with black magic fkery once i found out how to do it
    # https://stackoverflow.com/questions/41924002/how-do-i-run-the-pyglet-window-clear-function-through-a-on-button-press-event)
    pyglet.app.run()
