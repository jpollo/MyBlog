
粒子滤波步骤
-----------
1. 离子初始化

2. 重要性采样

3. 重采样（修正粒子权值）


条件
-----
1. 有观测值

	量测信息进行修正预测

2. 运动模型

3. 粒子滤波估值


问题
------
* 粒子多样性匮乏

	高斯粒子滤波

*


确定状态空间，建立系统状态向量的经验条件分布，从经验条件分布中采集样本
用量测信息更新重要性采样函数，重新采样粒子，更新权值和粒子状态