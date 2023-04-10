import time
from cocos.director import director
from cocos.layer import ColorLayer

from personage.mushroom_evil import state

KEY_W = 119
KEY_A = 97
KEY_D = 100
KEY_S = 115
KEY_Q = 113
KEY_SPACE = 32


class MainLayer(ColorLayer):
    def __init__(self, r=0, g=0, b=0, a=255):
        super(MainLayer, self).__init__(r, g, b, a)
        self.is_event_handler = True

    def on_draw(self):
        pawn_1 = self.children_names.get('NeMario', None)
        pawn_2 = self.children_names.get('Mushroom_1', None)
        print(self.children_names)
        if pawn_1 is None or pawn_2 is None:
            return
        rect_1 = pawn_1.get_rect()
        rect_2 = pawn_2.get_rect()
        rect_1.height = 10
        print(rect_1.width, rect_1.height, rect_2.width, rect_2.height)
        if rect_1.get_bottom() <= rect_2.get_top():
            if rect_1.get_right() <= rect_2.get_right():
                if rect_1.get_right() >= rect_2.get_left():
                    pawn_2.image = pawn_2.our_image.get_region(*state['crushed'])

    def on_key_press(self, key, mod):
        if key == 65293:
            print(self.children_names)
            director.pop()
        else:
            print(key)
        pawn = self.children_names.get('NeMario', None)
        print(pawn)
        if pawn is None:
            return
        # if key == KEY_W:
        #     pawn.to_up()
        if pawn.actions:
            return
        elif key == KEY_A:
            pawn.to_left()
        elif key == KEY_D:
            pawn.to_right()
        elif key == KEY_S:
            pawn.to_down()
        elif key == KEY_SPACE:
            pawn.jump()
            print(self.children)
        elif key == KEY_Q:
            pawn.attack()

    def on_key_release(self, key, mod):
        pawn = self.children_names.get('NeMario', None)
        if pawn is None:
            return
        elif key == KEY_A:
            pawn.stop_left()
        elif key == KEY_D:
            pawn.stop_right()
        elif key == KEY_S:
            pawn.stop_down()
        elif key == KEY_Q:
            pawn.stop_attack()






