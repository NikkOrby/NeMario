import time
from cocos.actions import JumpBy, Repeat, MoveBy
from pyglet.image import load
from Pawn import Pawn

state_small_1 = {
    'stay': (600, 260, 120, 70),
    'run_1': (90, 260, 120, 70),
    'run_2': (175, 260, 120, 70),
    'run_3': (270, 260, 120, 70),
    'run_4': (365, 260, 120, 70),
    'jump': (470, 260, 120, 70)
}

state_small_2 = {
    'stay': (
        (600, 230, 120, 70)
    ),
    'run': (
        (90, 230, 120, 70),
        (175, 230, 120, 70),
        (270, 230, 120, 70),
        (365, 230, 120, 70),
    ),
    'jump': (
        (470, 230, 120, 70)
    )
}


class Nemario(Pawn):
    def __init__(self):
        self.our_image = load('Personage/sprite/nemario.png')
        self.state_type = 'stay'
        self.current_state = 0
        super().__init__(image=self.our_image.get_region(*state_small_1['stay']), position=(180, 180), scale=0.5)
        self.is_fliped = False

    # def change_current_state(self, state_small, state_type):
    #     if state_type != self.state_type:
    #         self.state_type = state_type
    #     if len(state_small[state_type]) > 1:
    #         if self.current_state < len(state_small[state_type])-1:
    #             time.sleep(0.1)
    #             self.current_state += 1
    #
    #         else:
    #             self.current_state = 0

    def to_left(self):
        move = MoveBy((-60, 0), 1)
        move = Repeat(move)
        self.do(move)
        # self.change_current_state(state_small, 'run')
        self.image = self.our_image.get_region(*state_small_1['run_1'])
        self.image = self.image.get_transform(flip_x=True)
        self.is_fliped = True

    def to_right(self):
        move = MoveBy((60, 0), 1)
        move = Repeat(move)
        self.do(move)
        self.image = self.our_image.get_region(*state_small_1['run_1'])
        self.image = self.image.get_transform(flip_x=False)
        self.is_fliped = False

    def to_down(self):
        move = MoveBy((0, -60), 1)
        move = Repeat(move)
        self.do(move)
        self.image = self.our_image.get_region(*state_small_1['run_1'])
        self.image = self.image.get_transform(flip_x=False)
        self.is_fliped = False

    def jump(self):
        if self.is_fliped:
            jump = JumpBy((-100, 0), 100, 1, 2)
            self.image = self.our_image.get_region(*state_small_1['jump'])
            self.image = self.image.get_transform(flip_x=True)
        else:
            jump = JumpBy((100, 0), 100, 1, 2)
            self.image = self.our_image.get_region(*state_small_1['jump'])
            self.image = self.image.get_transform(flip_x=False)
        self.do(jump)

    # def stop_up(self):
    #     if self.actions:
    #         self.remove_action(self.actions[0])

    def stop_left(self):
        self.image = self.our_image.get_region(*state_small_1['stay'])
        self.image = self.image.get_transform(flip_x=True)
        if self.actions:
            self.remove_action(self.actions[0])

    def stop_right(self):
        self.image = self.our_image.get_region(*state_small_1['stay'])
        if self.actions:
            self.remove_action(self.actions[0])

    def stop_down(self):
        self.image = self.our_image.get_region(*state_small_1['stay'])
        if self.actions:
            self.remove_action(self.actions[0])




