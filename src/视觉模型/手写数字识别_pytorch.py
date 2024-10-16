# -*- coding: utf-8 -*-

"""
@author: miracle
@version: 1.0.0
@license: Apache Licence
@file: 手写数字识别_tensorflow.py
@time: 2023/9/4 14:42
"""


import time
import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.utils.data as Data
import torchvision
import matplotlib.pyplot as plt
import cv2

EPOCH = 1                 # 迭代次数
BATCH_SIZE = 50           # 每一批训练的数据大小
LR = 0.001                # 学习率
DOWNLOAD_MNIST = True    # 是否需要下载数据集，首次运行需要把该参数指定为True

train_data = torchvision.datasets.MNIST(root='./mnist',
                           train=True,
                           transform=torchvision.transforms.ToTensor(),
                           download=DOWNLOAD_MNIST)


# 查看数据size
# print(train_data.data.size())
# # 查看标签size
# print(train_data.targets.size())n
# # 在画布上展示图片
# plt.imshow(train_data.data[0].numpy(), cmap='gray')
# # 设置标题, %i 代表转为有符号的十进制
# plt.title('%i' % train_data.targets[0])
# plt.show()

# 训练集分批
train_loader = Data.DataLoader(dataset=train_data,
                batch_size=BATCH_SIZE,
                shuffle=True)

# 下载测试集数据
test_data = torchvision.datasets.MNIST(root='./mnist', train=False)

'''
    这里的test_data.data的size是(10000, 28, 28)
    维度一 表示测试集总数
    维度二 表示第多少个像素的横坐标对应的RGB值（这里已从三层(xxx,xxx,xxx)转为一层(k), k的值是0到1之间）
    维度三 与参数二相似，表示的是纵坐标
    添加维度(图片特征的高度)并切片后，test_x的size是(2000, 1, 28, 28)
    PyTorch图层以Torch.FloatTensor作为输入，所以这里要指定一下torch.float32，否则在后续的训练中会报错。
    最后除255是因为像素点是0-255范围的，这样可以做归一化处理，把特征值固定在0-1范围区间。如果不做
    归一化处理，会在某些情况下（比如RNN神经网络）出现欠拟合的问题。
'''
test_x = torch.unsqueeze(test_data.data, dim=1).type(torch.FloatTensor)[:2000]/255
# 获取正确分类的结果
test_y = test_data.targets[:2000]

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        '''
            对于nn.Conv2d中的padding参数，单独解释一下。
            把每个像素点当成一个特征，图像为28*28个像素，以长宽为5，步长为1的过滤器去扫描时，x轴方向，
            第一次扫描的是1~5个像素点（作为下一层神经网络的第1个特征），第二次扫描的是第2~6个像素点（作为下一层
            神经网络的第2个特征）……，最后一次扫描的是第24~28个像素点（作为下一层神经网络的第24个特征），会发现下一层
            比上一层少了4个特征。y轴方向也是同理。
            padding=2 表示在图像的四周都分别填充2个像素点。这样图像就变成了32*32个像素。
            此时按上述方式进行，会发现下一层的特征数量为28，这样就能保证两个神经网络层之间的特征数量相同。
            所以，想要 con2d 出来的图片长宽没有变化, padding=(kernel_size-stride)/2
        '''
        '''
            关于nn.MaxPool2d(kernel_size=2)
            把卷积后并经过激活函数的数据进行池化，MaxPooLing的方式池化（选取最大的一个像素点），
            池化的作用是压缩图片，筛选重要的特征信息。
            可以把它看成一个过滤器，kernel_size是过滤器的大小
        '''
        self.conv1 = nn.Sequential(
            nn.Conv2d(in_channels=1,
                      out_channels=16,
                      kernel_size=5,
                      stride=1,
                      padding=2),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(in_channels=16, out_channels=32, kernel_size=5, stride=1, padding=2),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)
        )
        self.out = nn.Linear(32 * 7 * 7, 10)

    def forward(self, x):
        x = self.conv1(x)  # n, 16, 14,14
        x = self.conv2(x)  # n, 32, 7, 7
        x = x.view(x.size(0), -1)  # n, 32 * 7 * 7
        output = self.out(x)       # n, 10
        return output

cnn = CNN()
optimizer = torch.optim.Adam(cnn.parameters(), lr=LR)
loss_func = nn.CrossEntropyLoss()

start_time = time.time()
for epoch in range(EPOCH):
    for step, (x, y) in enumerate(train_loader):
        b_x = Variable(x)
        b_y = Variable(y)

        output = cnn(x)
        loss = loss_func(output, b_y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if step % 50 == 0:
            test_output = cnn(test_x)
            pred_y = torch.max(test_output, 1)[1]
            accuracy = (sum(pred_y == test_y)).numpy()
            print('Epoch: ', epoch, '| train loass:%.4f' % loss.data.numpy(), '| test accuracy:%.2f' % accuracy)
            
# 使用训练好的模型，预测前十个数据，然后和真实值对比
test_output = cnn(test_x[:10])
pred_y = torch.max(test_output, 1)[1]
print(pred_y, ' prediction number')
print(test_y[:10], ' real number')

print('耗时:', time.time() - start_time)







































