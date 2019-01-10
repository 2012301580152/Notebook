import keras
import numpy as np
import matplotlib.pyplot as plt
#按顺序构成的模型
from keras.models import Sequential
#Dense全连接层
from keras.layers import Dense  
import pandas as pd 
#构建一个顺序模型
table= pd.read_table('data/data')

columns = table.columns

x_data = table[columns[:-1]].values
y_data = table[columns[-1]].values

model=Sequential()

#在模型中添加一个全连接层
#units是输出维度,input_dim是输入维度(shift+两次tab查看函数参数)
model.add(Dense(units=1,input_dim=9))   

#编译模型
model.compile(optimizer='sgd',loss='mse')   #optimizer参数设置优化器,loss设置目标函数

#训练模型
for step in range(3001):
    #每次训练一个批次
    cost=model.train_on_batch(x_data,y_data)
    #每500个batch打印一个cost值
    if step%500==0:
        print('cost:',cost)

#打印权值和偏置值
W,b=model.layers[0].get_weights()   #layers[0]只有一个网络层
print('W:',W,'b:',b)

#x_data输入网络中，得到预测值y_pred
y_pred=model.predict(x_data)

plt.scatter(x_data,y_data)

plt.plot(x_data,y_pred,'r-',lw=3)
plt.show()
