from pyglet.sprite import Sprite


class Fon(Sprite):
    def __init__(self, image, position=(0, 0), rotation=0, scale=1,
                 opacity=255, color=(255, 255, 255), anchor=None, z=1, **kwargs):
        super().__init__(image, position, rotation, scale,
                 opacity, color, anchor, **kwargs)
        self.z = z