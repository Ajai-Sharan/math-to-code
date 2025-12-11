import tensorflow as tf

vector_a = tf.constant(list(map(float, [1, 2, 3])))
vector_b = tf.constant(list(map(float, [4, 5, 6])))

scalar_factor = ((tf.tensordot(vector_a, vector_b, axes = 1))/ (tf.tensordot(vector_b, vector_b, axes = 1)))

result = scalar_factor * vector_b

print(result)
