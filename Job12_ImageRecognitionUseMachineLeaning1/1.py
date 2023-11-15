import tensorflow as tf
import random
# import matplotlib.pyplot as plt
tf.compat.v1.disable_eager_execution()
from tensorflow.keras.datasets import mnist

tf.random.set_seed(777)
# mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0


# parameters
learning_rate = 0.001
training_epochs = 15
batch_size = 100

# input place holders
X = tf.compat.v1.placeholder(tf.float32, [None, 784])
Y = tf.compat.v1.placeholder(tf.float32, [None, 10])

# weights & bias for nn layers
W1 = tf.Variable(tf.compat.v1.random_normal([784, 256]))
b1 = tf.Variable(tf.compat.v1.random_normal([256]))
L1 = tf.nn.relu(tf.matmul(X, W1) + b1)

W2 = tf.Variable(tf.compat.v1.random_normal([256, 256]))
b2 = tf.Variable(tf.compat.v1.random_normal([256]))
L2 = tf.nn.relu(tf.matmul(L1, W2) + b2)

W3 = tf.Variable(tf.compat.v1.random_normal([256, 10]))
b3 = tf.Variable(tf.compat.v1.random_normal([10]))
hypothesis = tf.matmul(L2, W3) + b3

# define cost/loss & optimizer
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
  logits=hypothesis, labels=Y
))
optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cost)

# initialize
sess = tf.compat.v1.Session()
sess.run(tf.compat.v1.global_variables_initializer())

# train my model
for epoch in range(training_epochs):
  avg_cost = 0
  total_batch = int(mnist.train.num_examples / batch_size)

  for i in range(total_batch):
      batch_xs, batch_ys = mnist.train.next_batch(batch_size)
      feed_dict = {X: batch_xs, Y: batch_ys}
      c, _ = sess.run([cost, optimizer], feed_dict=feed_dict)
      avg_cost += c / total_batch

  print('Epoch:', '%04d' % (epoch+1), 'cost = ', '{..9f}'.format(avg_cost))

print('Learning Finished')
