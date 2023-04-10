from cocos.actions import JumpBy, MoveBy, Repeat
from cocos.sprite import Sprite


class Pawn(Sprite):
    def __init__(self, image, position=(0, 0), rotation=0, scale=1,
                 opacity=255, color=(255, 255, 255), anchor=None, **kwargs):
        super().__init__(image, position, rotation, scale,
                 opacity, color, anchor, **kwargs)

    # def to_up(self):
    #     move = MoveBy((0, 60), 1)
    #     move = Repeat(move)
    #     self.do(move)
    #     self.is_fliped = False
















