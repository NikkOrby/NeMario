from cocos.actions import MoveBy, Repeat
from pyglet.image import load

from Pawn import Pawn

state = {
    'state_1': (0, 349, 40, 40),
    'state_2': (30, 349, 40, 40),
    'crushed': (75, 349, 40, 40)
}


class Mushroom(Pawn):
    def __init__(self):
        self.our_image = load('Personage/sprite/evil.png')
        super().__init__(image=self.our_image.get_region(*state['state_1']), position=(280, 180), scale=1)
        self.move()

    def move(self):
        move = MoveBy((20, 0), 1)
        move = Repeat(move)
        self.do(move)
