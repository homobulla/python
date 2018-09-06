

import shutil
import os
index = 'index.html'
static = 'static'
PATH = 'C:/Users/fengxj/Desktop/ftoul-debit/dist/'  # 需要移动的文件或文件夹地址
TARGET = 'E:/fyd_api_cloud/fyd_api_cloud/fyd_api_cloud/app/src/main/assets/widget/'  # 移动到的地方

'''
 移动文件
source 是文件或文件名称，与PATH配合确定路径
'''


def move_replace(source):
    source = PATH + source
    if os.path.exists(source):
        shutil.move(source, TARGET)
    else:
        print('not have source!')


'''
 删除原有文件，没找到覆盖的权限方法
 f 同样是移动目标的文件夹名或文件名
'''


def deletFlie(f):
    file = TARGET + f
    if os.path.isdir(file) & os.path.exists(file):
        # 文件夹
        shutil.rmtree(file)
    elif os.path.exists(file) & os.path.isfile(file):
        # 文件
        os.remove(file)
    else:
        print('not exists ' + file + '文件或文件夹')
    move_replace(f)


deletFlie(index)
deletFlie(static)

# move_replace(index)
# PATH = 'C:/Users/fengxj/Desktop/ftoul-debit/dist/static',
#         'C:/Users/fengxj/Desktop/ftoul-debit/dist/index.html']
# targe = ['E:/fyd_api_cloud/fyd_api_cloud/fyd_api_cloud/app/src/main/assets/widget/index.html',
#          'E:/fyd_api_cloud/fyd_api_cloud/fyd_api_cloud/app/src/main/assets/widget/static']


# def deletFlie(arr):

#     for file in arr:
#         if os.path.isdir(file) & os.path.exists(file):
#             shutil.rmtree(file)
#         elif os.path.exists(file) & os.path.isfile(file):
#             os.remove(file)
#         else:
#             print('not exists' + file + '文件或文件夹')


# def move_replace(Arr, targetPath='e:/'):
#     """
#     一个移动文件及文件夹的方法
#     Arr参数为一个列表：多个传参
#     targetPath为移动目标文件夹
#     """
#     for file in Arr:
#         # 先判断是否是个文件及是否真实存在
#         if os.path.isdir(file) & os.path.exists(file):
#             shutil.move(
#                 file, "E:/fyd_api_cloud/fyd_api_cloud/fyd_api_cloud/app/src/main/assets/widget")
#         elif os.path.exists(file) & os.path.isfile(file):
#             shutil.move(
#                 file, "E:/fyd_api_cloud/fyd_api_cloud/fyd_api_cloud/app/src/main/assets/widget")
#         else:
#             print('not exists' + file + '文件或文件夹')


# deletFlie(targe)
# move_replace(PATH)
