
from cocos import director,layer,scene,sprite,text
import time

director.director.init()

lable = text.Label("cocodnode",font_size = 12,anchor_x="center",anchor_y='center')
lable.tag = 300

main_layer = layer.Layer()
main_layer.add(lable)

cat_sprite = sprite.Sprite("imgs/cat.png")
cat_sprite.tag = 100
box_sprite = sprite.Sprite("imgs/box_bg.png")
box_sprite.tag = 200

w,h = director.director.get_window_size()
cat_sprite.position = (w//2,h//2)
box_sprite.position = (w//2,h//2)
lable.position = (w//2,h//2+140)

main_layer.add(cat_sprite,z=100,name="cat")
main_layer.add(box_sprite,z=50,name='box')

cat = main_layer.get('cat')
#print(cat.tag)
#main_layer.remove(cat)

childrens  = main_layer.get_children()
for x in childrens:
    print(x.tag)
cat.kill()

main_scene = scene.Scene(main_layer)
director.director.run(main_scene)
