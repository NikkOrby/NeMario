import cocos
from basic_layers import MainLayer


class IntroLayer(MainLayer):
    def __init__(self):
        super(IntroLayer, self).__init__(b=250)
        label_1 = cocos.text.Label(
            text="NoMario",
            position=(320, 340),
            font_name="Times New Roman",
            font_size=60,
            anchor_x="center",
            anchor_y="center")
        label_2 = cocos.text.Label(
            text="Нажмите enter для продолжения",
            position=(320, 40),
            font_name="Times New Roman",
            font_size=10,
            anchor_x="center",
            anchor_y="center")
        self.add(label_1, z=1, name='title')
        self.add(label_2, z=2, name='offer')
        # self.is_event_handler = True

