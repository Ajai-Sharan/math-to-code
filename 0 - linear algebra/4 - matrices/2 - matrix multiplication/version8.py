
import tensorflow as tf

tensor_a = tf.constant([[1, 2, 3], [4, 5, 6]])
tensor_b = tf.constant([[7, 8], [9, 1], [2, 3]])

# Method 1: The @ operator
result = tensor_a @ tensor_b

# Method 2: matmul function
result_mm = tf.linalg.matmul(tensor_a, tensor_b)

print(result)