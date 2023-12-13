import tensorflow as tf 
import random
from tensorflow.keras.datasets import mnist

tf.compat.v1.disable_eager_execution()
tf.compat.v1.set_random_seed(777)  # reproducibility 

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Flatten the images and normalize pixel values to the range [0, 1]
x_train = x_train.reshape([-1, 784]) / 255.0
x_test = x_test.reshape([-1, 784]) / 255.0

# Convert labels to one-hot encoding
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

# hyper parameters
learning_rate = 0.001
training_epochs = 15
batch_size = 100

# input place holders
X = tf.compat.v1.placeholder(tf.float32, [None, 784])
X_img = tf.reshape(X, [-1, 28, 28, 1])  # img 28x28x1 (black/white) 
Y = tf.compat.v1.placeholder(tf.float32, [None, 10])

# -------------- Cấu trúc tầng mạng --------------
# Lớp Convolutional Đầu Tiên
W1 = tf.Variable(tf.random.normal([3, 3, 1, 32], stddev=0.01))
L1 = tf.nn.conv2d(X_img, W1, strides=[1, 1, 1, 1], padding='SAME')
L1 = tf.nn.relu(L1)
L1 = tf.nn.max_pool(L1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

# Lớp Convolutional Thứ Hai
W2 = tf.Variable(tf.random.normal([3, 3, 32, 64], stddev=0.01))
L2 = tf.nn.conv2d(L1, W2, strides=[1, 1, 1, 1], padding='SAME')
L2 = tf.nn.relu(L2)
L2 = tf.nn.max_pool(L2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
L2_flat = tf.reshape(L2, [-1, 7 * 7 * 64])

# Lớp Fully Connected (1)
W3 = tf.Variable(tf.random.normal([7 * 7 * 64, 10], stddev=0.01))
b = tf.Variable(tf.random.normal([10]))
logits = tf.matmul(L2_flat, W3) + b

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=Y))
optimizer = tf.compat.v1.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

# initialize
sess = tf.compat.v1.Session()
sess.run(tf.compat.v1.global_variables_initializer())

# train my model
print("Learning started. It takes sometime.")
for epoch in range(training_epochs):
    avg_cost = 0
    total_batch = int(x_train.shape[0] / batch_size)
    for i in range(total_batch):
        batch_xs, batch_ys = x_train[i * batch_size:(i + 1) * batch_size], y_train[i * batch_size:(i + 1) * batch_size]
        feed_dict = {X: batch_xs, Y: batch_ys}
        c, _ = sess.run([cost, optimizer], feed_dict=feed_dict)
        avg_cost += c / total_batch
    print('Epoch:', '%04d' % (epoch + 1), 'cost=', '{:.9f}'.format(avg_cost))
print("Learning Finished!")

# Test model and check accuracy
correct_prediction = tf.equal(tf.argmax(logits, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print('Accuracy:', sess.run(accuracy, feed_dict={X: x_test, Y: y_test}))

# Get one and predict
r = random.randint(0, x_test.shape[0] - 1)

print("Label: ", sess.run(tf.argmax(y_test[r:r + 1], 1)))
print("Prediction:", sess.run(tf.argmax(logits, 1), feed_dict={X: x_test[r:r + 1]}))
