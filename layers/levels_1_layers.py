from personage.mushroom_evil import Mushroom
from personage.nemario import Nemario
from static.block import Block
from basic_layers import MainLayer


class Levels1(MainLayer):
    def __init__(self):
        super(Levels1, self).__init__(0, 0, 250, 255)
        nemario = Nemario()
        mushroom = Mushroom()
        block_1 = Block()
        self.add(nemario, z=2, name='NeMario')
        self.add(mushroom, z=2, name='Mushroom_1')
        self.add(block_1, name='Block_1')
        print(self.get_children())
        mushroom_get_rect = mushroom.get_rect()
        mushroom_get_rect.height = 10





