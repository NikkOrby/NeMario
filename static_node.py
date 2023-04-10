from pyglet.sprite import Sprite


class StaticNode(Sprite):
    def __init__(self, image, position=(0, 0), rotation=0, scale=1,
                 opacity=255, anchor=None, **kwargs):
        super().__init__(image, position, rotation, scale,
                 opacity, anchor, **kwargs)
