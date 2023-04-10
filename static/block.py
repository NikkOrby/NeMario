from pyglet.image import load

from static_node import StaticNode


class Block(StaticNode):
    def __init__(self):
        self.our_image = load('Static/sprite/static.png')
        print(self.our_image.get_region(300, 300, 70, 70))
        print(self.our_image)
        super().__init__(image=self.our_image.get_region(300, 300, 70, 70), position=(180, 180), scale=0.5)

