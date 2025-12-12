import tensorflow as tf

matrix = tf.constant(   [[2., 3., 1.],
                        [4., 1., -3.],
                        [5., -2., 0.]] )

inverse = tf.linalg.inv(matrix)
det = tf.linalg.det(matrix)

adjoint = det * inverse

print(adjoint)