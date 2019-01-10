# 常用目标函数
## 误差平方和准则
$$
S = \sum_{j=1}^{n}(Q-\hat{Q})_{j}^{2}=min
$$
## 误差绝对值和准则

$$
S = \sum_{j=1}^{n}|Q-\hat{Q}|_j
$$

## 确定性系数准则

$$
d_Q=1-\frac{s_\sigma^2}{\sigma_Q^2}
$$

$$
s_\sigma = \sqrt{\frac{\sum{(Q-\hat{Q})^2}}{n}}
$$

$$
\sigma_Q=\sqrt{\frac{\sum{(Q-\bar{Q})^2}}{n}}
$$

## 洪峰预报合格率准则

$$
\delta=|\frac{\hat{Q}_i-Q_i}{Q_i}|\times100\%
$$

如果$\delta_\sigma$是范围运行的最大相对误差，则洪峰预报合格率为：
$$
\mathcal{p}(\delta_i\leqslant\delta_\sigma) = \frac{m}{n}\times100\%\leqslant\mathcal{p}(\delta_\sigma)
$$
