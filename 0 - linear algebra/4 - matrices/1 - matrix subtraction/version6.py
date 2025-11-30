
import tensorflow as tf

matrix_a = tf.constant([[1, 2, 3], [4, 5, 6]])
matrix_b = tf.constant([[7, 8, 9], [10, 11, 12]])

result = matrix_a - matrix_b

result_func = tf.subtract(matrix_a, matrix_b)

print(result)
print(result_func)