import cocos

from cocos.actions import *

class HelloWorld(cocos.layer.ColorLayer):
	def __init__(self):
		# blueish colour
		super(HelloWorld, self).__init__(64, 64, 225, 255)

label = cocos.text.Label('Hello World!', anchor_x='center', anchor_y='center')

# set the label in the centre of the screen
label.position = 320, 240
self.add(label)

sprite = cocos.sprite.Sprite('Xan.png')
sprite.position = 320, 240
sprite.scale = 3

self.add(sprite, z=1)

scale = ScaleBy(3, duration=2)

label.do(Repeat(scale + Reverse(scale)))
sprite.do(Repeat(Reverse(scale) + scale))

cocos.director.director.init()
hello_layer = HelloWorld()

hello_layer.do(RotateBy(360, duration=10))

# A scene that contains the layer Hello_layer
main_scene = cocos.scene.Scene(hello_layer)
# And now, starting the app, starting with the main sc
cocos.director.director.run(main_scene)