import tensorflow as tf

tensor_m = tf.constant([[1, 2, 3], [4, 5, 6]])

# Method 1: standard transpose
result = tf.transpose(tensor_m)

# Method 2: permute equivalent (specifying order)
result_perm = tf.transpose(tensor_m, perm=[1, 0])

print(result)