import cv2
import numpy as np


def show_pic(img):
    cv2.imshow('pic', img)
    cv2.waitKey()


def complement(img):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i, j] = 255 - img[i, j]
    return img

# ----------------------- Number 5 -------------------
images = []
for i in range(15):
    img = cv2.imread(f'hw2/highway/h{i}.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img = img // 14
    images.append(img)

empty = np.zeros((images[0].shape[0], images[0].shape[1]))

empty = sum(images)

# show_pic(empty)

# ----------------------- Number 3 -------------------
board_orig = cv2.imread('hw2/board - origin.bmp')
board_test = cv2.imread('hw2/board - test.bmp')

board_orig = cv2.cvtColor(board_orig, cv2.COLOR_RGB2GRAY)
board_test = cv2.cvtColor(board_test, cv2.COLOR_RGB2GRAY)

board_test = cv2.flip(board_test, 1)

diff = cv2.subtract(board_orig, board_test) * 5

# show_pic(diff)

# ----------------------- Number 2 -------------------

images = []
for folder in range(4):
    result = []

    for img_num in range(5):
        img = cv2.imread(f'hw2/black hole/{folder+1}/{img_num+1}.jpg')
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        result.append(img // 5)

    images.append(sum(result))

last_pic = cv2.vconcat([ (cv2.hconcat([images[0], images[1]])) , cv2.hconcat([images[2], images[3]]) ])
cv2.imwrite('galaxy.jpg', last_pic)

# show_pic(last_pic)

# ----------------------- Number 1 -------------------
a = cv2.imread('hw2/a.tif')
b = cv2.imread('hw2/b.tif')

a = cv2.cvtColor(a, cv2.COLOR_RGB2GRAY)
b = cv2.cvtColor(b, cv2.COLOR_RGB2GRAY)
b = 255 - b
a = 255 - a

# show_pic(cv2.subtract(a, b))

# ----------------------- Number 4 -------------------
image_chess = cv2.imread('hw2/chess pieces.jpg')
image_chess = cv2.cvtColor(image_chess, cv2.COLOR_RGB2GRAY)

buffer = []
counter = 0
chess_images = []
for column_num in range(image_chess.shape[1]):
    column_data = []
    for i in range(image_chess.shape[0]):
        if image_chess[i, column_num] > 200:
            column_data.append(image_chess[i, column_num])
    if len(column_data) == image_chess.shape[0]:
        counter += 1
    else:
        buffer.append(image_chess[:, column_num])

    if counter > 10 and len(buffer) > 10:
        chess_images.append(buffer)
        counter = 0
        buffer = []
        # print(column_num)

for pic in range(len(chess_images)):
    ch = np.zeros([chess_images[pic][0].shape[0], len(chess_images[pic])], dtype=np.uint8)
    for z in range(len(chess_images[pic])):
        ch[:, z] = chess_images[pic][z]
    # show_pic(ch)
    # cv2.imwrite(f'hw2/chess/chess{pic}.jpg', ch)

# ----------------------- Number 6 -------------------
image_mona = cv2.imread('hw2/Mona_Lisa.jpg')
image_mona = cv2.cvtColor(image_mona, cv2.COLOR_RGB2GRAY)


filter_ = np.ones([image_mona.shape[0], image_mona.shape[1]], dtype=np.uint8)
print(filter_.shape)

for i in range(filter_.shape[0]):
    z = 1
    for j in range(0, filter_.shape[1], 2):
        filter_[i, j] = z
        filter_[i, j+1] = z
        z += 1
filter_[filter_ == 0] = 255

show_pic(image_mona / filter_)

