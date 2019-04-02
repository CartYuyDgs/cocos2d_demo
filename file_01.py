
import cocos

class Mylayer(cocos.layer.Layer):
    def __init__(self):
        super(Mylayer, self).__init__()
        label = cocos.text.Label("forever nice",font_size = 36,anchor_x ="center",anchor_y="center")
        label.position = (320,240)
        self.add(label)


if __name__ == '__main__':
    director = cocos.director.director
    director.init(caption="abc")
    main_layer = Mylayer()
    main_scene = cocos.scene.Scene(main_layer)
    director.run(main_scene)