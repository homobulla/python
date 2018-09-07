# -*- coding:utf-8 -*-

import os
from PIL import Image


path1 = os.path.abspath('.')  # 当前路径


def get_imlist(path):
    """返回目录中所有png图像的文件名列表"""
    return [os.path.join(path, f) for f in os.listdir(path)
            if f.endswith(".png")]


def save_change(save_dir, n, x1, y1, x2, y2):
    box = (x1, y1, x2, y2)
    # 区域由一个4元组定义，表示为坐标是 (left, upper, right, lower)。
    # Python Imaging Library 使用左上角为 (0, 0)的坐标系统。
    # 同时要注意，这些坐标指向像素之间的位置，因此上述例子中描述的区域的大小为300x300像素。
    region = pil_im.crop(box)

    save_dir = save_dir + str(n) + ".png"
    region.save(save_dir)


if __name__ == "__main__":

    """
    path 图片源路径
    """
    path = path1 + "/demo/demo1/resouce"
    print(path)
    exit()
    listdir = get_imlist(path)  # 获取路径下的所有图片

    for dir in listdir:
        infile = os.path.splitext(dir)[0]

        infile = infile.replace("resouce", "result")
        save_dir = infile + "_"

        # quit()  # js return
        pil_im = Image.open(dir).convert('L')

        # 这里我需要得到图片尺寸以一定比列来切割图片
        size = pil_im.size
        # 返回元组(1333,2323)
        save_change(save_dir, 1, 0, 0, size[0]/2, size[1]/2, )
        save_change(save_dir, 2, size[0]/2, 0, size[0], size[1]/2)

        save_change(save_dir, 3, 0, size[1]/2, size[0]/2, size[1], )
        save_change(save_dir, 4, size[0]/2, size[1]/2, size[0], size[1])
