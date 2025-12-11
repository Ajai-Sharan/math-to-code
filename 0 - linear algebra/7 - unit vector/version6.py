import tensorflow as tf

tensor_v = tf.constant([3., 4.])

# Method 1: Manual Math
unit_v = tensor_v / tf.norm(tensor_v)

# Method 2: Dedicated Function
# axis=0 means normalize across the vector
unit_v_func = tf.math.l2_normalize(tensor_v, axis=0)

print(unit_v_func)