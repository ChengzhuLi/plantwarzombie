import random

import pygame

class Sun(pygame.sprite.Sprite):
    def __init__(self,rect):
        super(Sun,self).__init__()
        self.image = pygame.image.load('material/images/Sun_1.png').convert_alpha()
        # 返回surface对象
        # 返回的 Surface  对象将包含与源文件相同的颜色格式，colorkey 和 alpha 透明度通道。
        # 你通常需要调用 Surface.convert() 函数进行转换，这样可以使得在屏幕上绘制的速度更快。
        # 对于含有 alpha 通道的图片（支持部分位置透明，像 PNG 图像），需要使用 Surface.convert_alpha() 函数进行转换。
        self.images = [pygame.image.load('material/images/Sun_{}.png'.format(i)).convert_alpha() for i in range(1,18)]
        # 应该使用 os.path.join() 提高代码的兼容性：
        self.rect = self.images[0].get_rect()
        # get_rect返回一个元组，长方形属性
        # 确定位置补偿
        offsetTop = random.randint(-50,50)
        offsetLeft = random.randint(-50,50)

        self.rect.top = rect.top + offsetTop
        self.rect.left = rect.left + offsetLeft

    def update(self, *args):

        # 对于太阳图片来说，一共17张，编号0-16
        # args[0]是提取当前图片但不确定第几张，
        # 如果取余长度17，对应的余数就是第几张图片
        # 这样可以展现动画，因为更新是直接显示在屏幕上的
        self.image = self.images[args[0] % len(self.images)]

