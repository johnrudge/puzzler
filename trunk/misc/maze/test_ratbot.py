import visual
import ratbot

visual.box(length=10, height=10, width=.1, pos=(0, 0, -.5), color=(.8, .8, 1))

rat = ratbot.RatBot()

while 1:
    for i in range(3):
        rat.advance()

    rat.turn_left()
    for i in range(3):
        rat.advance()

    rat.turn_left()
    for i in range(6):
        rat.advance()

    rat.turn_left()
    for i in range(6):
        rat.advance()
        rat.turn_left()
        rat.advance()
        rat.turn_right()

    rat.turn_right()
    for i in range(3):
        rat.advance()

    rat.turn_right()
    for i in range(3):
        rat.advance()

    rat.turn_left()
