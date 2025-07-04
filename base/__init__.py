# tensorflow框架的测试验证案例
import tensorflow as tf

# 简单测试代码
print("TensorFlow version: ", tf.__version__)
a = tf.constant(1)
b = tf.constant(2)
c = a + b
print("Simple addition result: ", c.numpy())
