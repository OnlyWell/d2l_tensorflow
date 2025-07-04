# 机器学习开发流程
    大体分为10个步骤(比较粗略):
1. 搜集数据,汇整成为数据集(DataSet)
2. 数据清理(Data Cleaning)、数据探索与分析(Exploratory Data Analysis,EDA):EDA通常是指以描述统计量与统计图观察数据的分布,了解数据的特性、
极端值(Outlier)、变量之间的关联性
3. 特征工程(Featire Engineering): 原始搜集的数据未必是影响预测目标的关键因素,有时候需要进行数据转换,以找到关键的影响变量。
4. 数据切割(Data split): 切割为训练数据(Traning Data)及测试数据(Test Data),一份数据提供模型训练之用,另一份数据用于衡量模型效果,即准确度。
切割的主要目的是确保测试数据不会参与训练,以维持其公正性,即Out-of-Sample Test
5. 选择算法(Learning Algorithms): 依据问题的类型选择适合的算法
6. 模型训练(Model Traning): 以算法及训练数据进行训练,产出模型
7. 模型计分(Score Model): 计算准确度等效果指标,评估模型的准确性
8. 模型评估(Evaluate Model): 比较多个参数组合、多个算法的准确度,找到最佳参数与算法
9. 部署(Deploy): 复制最佳模型至正式环境(Production  Environment),制作使用界面或提供API,通常以网页服务(Web Services)作为预测的API。
10. 预测(Predict): 客户端传入新数据或文件,系统以模型进行预测,传回预测结果