import tensorflow as tf

tensor_m = tf.constant([[4., 7.], [2., 6.]])

# Method 1: Exact Inverse
inverse = tf.linalg.inv(tensor_m)

# Method 2: Pseudo-Inverse
pinverse = tf.linalg.pinv(tensor_m)

print(inverse)