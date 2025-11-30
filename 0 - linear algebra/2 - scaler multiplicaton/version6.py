
import tensorflow as tf

vector = tf.constant([1,2,3])

scalar = 10

result_v1 = vector * scalar

result_v2 = tf.math.multiply(vector, scalar)

print(result_v1)
print(result_v2)
