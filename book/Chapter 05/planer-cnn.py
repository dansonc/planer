from planer import *  

class CNN(Net):  
    def __init__(self):  
        self.relu = ReLU()
        self.softmax = Softmax()
        self.flaten = Flatten()
        # 1通道输入，32个卷积，卷积核大小3
        self.conv1 = Conv2d(1, 32, 3)
        # 窗口大小2，stride2的最大池化 
        self.pool1 = Maxpool(2, 2)
        self.conv2 = Conv2d(32, 64, 3)
        self.pool2 = Maxpool(2, 2)
        self.conv3 = Conv2d(64, 64, 3)
        self.fc1 = Dense(64*7*7, 512)
        self.fc2 = Dense(512, 10)
        
    def forward(self, x):  
        x = self.conv1(x)
        x = self.relu(x)
        x = self.pool1(x)
        x = self.conv2(x)
        x = self.relu(x)
        x = self.pool2(x) 
        x = self.conv3(x)
        x = self.relu(x)
        x = self.flaten(x)     
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return self.softmax(x)

model = CNN()
x = np.zeros((1, 1, 28, 28), dtype='float32')
y = model(x)
print(x.shape, y.shape)    

