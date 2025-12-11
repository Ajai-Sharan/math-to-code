import tensorflow as tf

tensor_m = tf.constant([[6., 1., 1.], [4., -2., 5.], [2., 8., 7.]])

# Calculate Determinant
result = tf.linalg.det(tensor_m)

print(result)