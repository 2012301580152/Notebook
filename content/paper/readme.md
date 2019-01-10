# 降雨径流关系分析

摘要

山洪灾害常造成重大经济损失甚至人员伤亡。以官山河流域为例,基于地理信息系统和遥感技术的水文模型集成系统为山洪预报提供了新的思路,在解译了研究流域2010年土地利用类型数据的基础上,采用HEC-HMS水文模型对武水流域各场次洪水进行模拟预报,利用DEM及流域出口信息划分子流域计算单元,利用遥感影像结合GIS技术提取流域信息,采用SCS径流曲线法进行产流计算,采用SCS单位线法计算直接径流,利用马斯京根法进行河道汇流演进,运用指数退水模型模拟流域基流,并以2000—2008年的17场实测洪水数据进行参数的率定,用2009—2014年的10场典型洪水进行验证。结果表明:模型率定期17场洪水洪峰流量相对误差绝对值均<20%,模拟合格率达到100%,峰现时差均≤1 h,绝对平均Nash效率系数为0.816,率定出的水文参数准确有效;验证期的10场洪水,洪峰流量相对误差合格率达90%,峰现时差均<1 h,Nash效率系数均>0.7。HEC-HMS水文模型在武水流域模拟效果较好,可应用于该流域山洪预报工作,且相较于多峰洪水,单峰洪水的模拟效果更佳。 



官山河为汉江中上游，其流域位于丹江口市西南部，河长66.5千米，流域面积465平方千米，孤山水文站以上流域面积300多km2。流域平均高程690米，河道平均坡降5.7‰，多年平均流量7.78立方米每秒。



## 长期短期记忆（LSTM）模型在官山河洪水预报上的应用 

摘要

在多变的气候条件以及复杂的地理要素下，水文预报是一项极具挑战性的工作。为了应对这一挑战，水文工作者在水文预报上开展了大量的工作，包括统计计算，水文机理探究和数据驱动方法等。深度学习算法作为数据驱动方法方面最热门的方法，在水文时间序列预测上有着相当大的应用前景。因此，有必要研究深度学习算法在水文预报上的应用。长短期记忆（LSTM）网络在水文学领域的适用性有着明显的优势。LSTM网络是一种特殊的递归神经网络（RNN），它在神经元之间建立连接并形成有向循环。LSTM克服RNN的弱点，以学习长期的依赖关系，有很好的长时间记忆效果。本研究，我们以官山河流域为例， 研究新型深度学习方法在山洪预报上的应用。分别构建传统水文模型及长短期记忆（LSTM）模型对官山河山洪过程进行模拟，并对比两种方案的模拟效果。以1976-1984年的实测洪水数据进行参数的率定，用1985-1987年的洪水进行验证。传统水文模型通过遗传算法率定参数；LSTM模型则通过构建不同的网络层，多个激励函数响应降雨径流非线性关系，构建确定目标的损失函数，应用梯度下降法计算出最优解。比较结果表明长短期记忆（LSTM）模型能够较好的模拟官山河流域山洪过程。



## Application of the long short-term memory network For Hydrologic forecasting On Guanshan river basin

abstract

Hydrologic forecasting is still a challenging task under changeable weather condition and complex geographical conditions. Many works including statistical, hydrological mechanism and data-driven on inflow forecasting have been developed to handle the complexity and planning. As the most popular method in data-driven, deep learning algorithm has considerable application prospects in hydrological forecasting. Therefore, it is necessary to identify the application of the deep learning algorithm to hydrological forecasting. Long short-term memory (LSTM) networks have obvious advantages in the applicability of hydrology. The LSTM network is a special recurrent neural network (RNN) that establishes connections between neurons and forms a directed loop. LSTM overcomes the weaknesses of RNN to learn long-term dependencies and has a good effect on long-term memory. In this study, we take the Guanshan River Basin as an example to discuss the application of the novel deep learning method in hydrologic forecasting. The conventional hydrological model and the long-term and short-term memory (LSTM) model were constructed to simulate the flood process of Guanshan River, and the simulation effects of the two schemes were compared. The parameters were determined using the measured flood data from 1976 to 1984 and verified by floods from 1985 to 1987. The conventional hydrological model uses the genetic algorithm to determine the parameters; The LSTM model responds the nonlinear relationship of rainfall runoff by constructing different network layers and multiple excitation functions，constructs the loss function of the target, and calculates the optimal solution by using the gradient descent method. The comparison results show that the long short-term memory (LSTM) model can worked well on hydrologic forecasting of the Guanshan River Basin.





 













官山河山洪模拟

模拟方法选择

topmodel洪水过程模拟

lstm洪水过程模拟

结果分析











应用官山河新安江水文模型通过遗传算法并且设置多层LSTM结构比较不同的误差函数





 并且以初损后损法为产流模块、Ｓｎｙｄｅｒ 单位线法为直接径流模块、退水曲线
法为基流计算模块、马斯京根法为河道汇流计算模块的方案在径流深精度、洪峰流量精度、峰现时差和确定性
系数上均略优于以ＳＣＳ 曲线法为产流计算模块、ＳＣＳ 单位线法为直接径流计算模块、退水曲线法为基流计算模
块、马斯京根法为河道汇流计算模块的组合方案。
关键词：水文模型； 恭城河流域； 洪水预报

















本文以官山河为例，研究新型深度学习方法在预测入库径流上的应用。目的是探讨长期短期记忆（LSTM）模型在预测入库径流模拟上的效果，建立一种新的LSTM模型，该模型通过误差修正进行工作。将两种模型的性能与水文领域的流行预测方法进行了比较。
结果表明，与其他常用的机器学习方法相比，所提出的新型LSTM模型在入境径流预测性能方面具有一定的优势。



山洪灾害常造成重大经济损失甚至人员伤亡。











在这项研究中，我们将LSTM网络应用于韩国每月大坝流入，以确定水文时间序列预测的适用性。此外，LSTM网络的性能与传统的水文时间序列预测模型进行了比较。最后，我们得出了几个结论，包括在月度大坝流入预测中应用LSTM网络的最佳条件。





   













abstarct





This study presents a case study of Guanshan river using a novel deep learning method to forecast the inbound runoff. The aim is to explore the potential of long short-term memory (LSTM) model in forecasting inbound runoff, and a novel LSTM model modified by error correction model is established. The performance of the two models is compared with popular prediction methods in the hydrology field.
Results show that the proposed novel LSTM model has slight advantages in level inbound runoff prediction performance comparing with other common machine learning methods. 



However, it outperforms other
models including original LSTM in terms of directional prediction accuracy, and accurately predicts the indoor
temperature variation trend. This work is enlightening and may have a further reference to the feasibility study
of indoor air temperature prediction model.





山区洪水降雨径流关系

考虑滞时性，和不考虑滞时性

## 多元线性回归



## ANN等非线性方法

## RNN等滞时性方法

## 综合分析





# 降雨分布计算





# 水文模型研究

降雨单位线的非线性问题



tank水文模型

tvgm

分布式水文模型

topmodel

水文模型机理研究
