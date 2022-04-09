# from matplotlib import image, pyplot
# import os
import numpy as np

# cwd = os.getcwd()
# utils = cwd+"\\project\\Utils\\"
# # load image as pixel array
# me_n_the_boys = image.imread(utils+'thinking_about_thinking.jpg')
# # summarize shape of the pixel array
# print(me_n_the_boys.dtype)
# print(me_n_the_boys.shape)
# # display the array of pixels as an image
# pyplot.imshow(me_n_the_boys)
# pyplot.show()
a = np.array([[2,2,2]])
b = a.T
print(a)
print(b)
c = np.matmul(b,a)
print(np.linalg.det(c))
x = np.array([[2,3,4]])
x = x.T
print(x)
print(type(x))