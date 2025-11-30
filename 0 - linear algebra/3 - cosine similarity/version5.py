import tensorflow as tf

tensor_a = tf.constant([1.0, 2.0, 3.0])
tensor_b = tf.constant([4.0, 5.0, 6.0])

# Manual math using TF ops (Safest for general use)
normalize_a = tf.nn.l2_normalize(tensor_a, 0)        
normalize_b = tf.nn.l2_normalize(tensor_b, 0)
cos_sim = tf.reduce_sum(tf.multiply(normalize_a, normalize_b))

print(cos_sim)