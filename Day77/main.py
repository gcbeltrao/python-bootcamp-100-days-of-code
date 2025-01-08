import numpy as np

import matplotlib.pyplot as plt
from scipy import misc
from PIL import Image
from numpy.random import random

# CLASS 602

# my_array = np.array([1.1, 9.2, 8.1, 4.7])

# array_2d = np.array([[1, 2, 3, 9], [5, 6, 7, 8]])

# mystery_array = np.array(
#     [
#         [[0, 1, 2, 3], [4, 5, 6, 7]],
#         [[7, 86, 6, 98], [5, 1, 0, 4]],
#         [[5, 36, 32, 48], [97, 0, 27, 18]],
#     ]
# )

# matrix = []

# print(f"Dimentions: {mystery_array.ndim}")
# print(
#     f"Shape: {mystery_array.shape}. It has {mystery_array.shape[2]} elements in each axis."
# )
# print(f"value 18: {mystery_array[2, 1, 3]}")
# print(f"1 dimensional vector: {mystery_array[2, 1, :]}")
# print(mystery_array[:, :, 0])

# CLASS 603

# a = np.arange(10, 30)
# print(a)

# last_three = a[-3:]
# print(last_three)

# subset_456 = a[3:6]
# print(subset_456)

# subset_minus12 = a[12:]
# print(subset_minus12)

# subset_even = a[::2]
# print(subset_even)

# b = np.array([6,0,9,0,0,5,0])
# nz_indices = np.nonzero(b)

# z = random((3,3,3))
# print(z)

# reversed_array = np.flip(a)
# print(reversed_array)

# x = np.linspace(0, 100, num=9)
# print(x)

# y = np.linspace(-3, 3, num=9)
# print(y)

# plt.plot(x, y)

# noise = random((128,128,3))
# print(noise.shape)
# plt.imshow(noise)

# CLASS 604

# a1 = np.array([[1, 3], [0, 1], [6, 2], [9, 7]])

# b1 = np.array([[4, 1, 3], [5, 8, 5]])

# c1 = np.matmul(a1, b1)
# print(c1)

# a1 @ b1

# CLASS 605

# img = misc.face()
# plt.imshow(img)
# type(img)
# img.shape
# img.ndim

# RGB_IMG = img / 255
# GREY_VALS = np.array([0.2126, 0.7152, 0.0722])
# img_gray = RGB_IMG @ GREY_VALS
# plt.imshow(img_gray, cmap='gray')


# RGB_IMG_inverted = np.flip(img) / 255
# img_gray_inverted = RGB_IMG_inverted @ GREY_VALS
# plt.imshow(img_gray_inverted, cmap='gray')


# RGB_IMG_rotated = np.rot90(img)
# plt.imshow(RGB_IMG_rotated)


# RGB_IMG_oposto = 255 - img
# plt.imshow(RGB_IMG_oposto)

my_img = Image.open('Foto-perfil.jpg')
img_array = np.array(my_img)

RGB_IMG = img_array / 255
GREY_VALS = np.array([0.2126, 0.7152, 0.0722])
img_gray = RGB_IMG @ GREY_VALS
plt.imshow(img_gray, cmap='gray')


RGB_IMG_inverted = np.flip(img_array) / 255
img_gray_inverted = RGB_IMG_inverted @ GREY_VALS
plt.imshow(img_gray_inverted, cmap='gray')


RGB_IMG_rotated = np.rot90(img_array)
plt.imshow(RGB_IMG_rotated)


RGB_IMG_oposto = 255 - img_array
plt.imshow(RGB_IMG_oposto)