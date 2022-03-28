from matplotlib import image, pyplot
import os

cwd = os.getcwd()
utils = cwd+"\\project\\Utils\\"
# load image as pixel array
me_n_the_boys = image.imread(utils+'thinking_about_thinking.jpg')
# summarize shape of the pixel array
print(me_n_the_boys.dtype)
print(me_n_the_boys.shape)
print(me_n_the_boys)
# display the array of pixels as an image
pyplot.imshow(me_n_the_boys)
pyplot.show()