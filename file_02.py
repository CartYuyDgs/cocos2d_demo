from cocos import director
from cocos import scene
from cocos import layer
from cocos import text



class Mylayer(layer.Layer):
    def __init__(self,x,y):
        super(Mylayer, self).__init__()
        label = text.Label("%s,%s"%(x,y),font_size=32,anchor_x='center',anchor_y='center')
        label.position = (240,280)
        self.add(label)

def main():
    director.director.init(caption="窗口",width=480,height=560,fullscreen=False,resizable=False)
    #main_layer = Mylayer()
    w,h = director.director.get_window_size()
    main_layer = Mylayer(w,h)
    main_scene = scene.Scene(main_layer)
    director.director.show_FPS = True
    director.director.run(main_scene)


if __name__ == '__main__':
    main()
