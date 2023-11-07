import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
sess = tf.Session()
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b
print(sess.run(adder_node, feed_dict={a:2, b:1.5}))
print(sess.run(adder_node, feed_dict={a:[2, 3], b:[1, 4]}))

# Cast a constant integer tensor into floating point.
float_tensor = tf.cast(tf.constant([1, 2, 3])),
dtype = tf.float(32)

3. # a rank 0 tensor; a scalar with shape [].
[1., 2., 3.] # a rank 1 tensor; a vector with shape [3]
[[1., 2., 3.], [4., 5., 6.]] # a rank 2 tensor; a matrix with shape [2, 3]
[[[1., 2., 3.]], [[7., 8., 9.]]] # a rank 3 tensor with shape [2, 1, 3]
