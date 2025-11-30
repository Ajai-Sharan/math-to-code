import tensorflow as tf

tensor_a = tf.constant([1, 2, 3])
tensor_b = tf.constant([4, 5, 6])

# tensordot is the most general way
# axes=1 tells it to sum over the first axis (standard dot product)
result = tf.tensordot(tensor_a, tensor_b, axes=1)

print(result)
