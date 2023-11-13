import tensorflow as tf
import matplotlib.pyplot as plt
import random

# Đặt giống ngẫu nhiên
tf.random.set_seed(777)

# Tải dữ liệu MNIST từ TensorFlow Datasets
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Chuẩn hóa dữ liệu và chuyển đổi thành one-hot encoding
x_train, x_test = x_train / 255.0, x_test / 255.0
y_train = tf.one_hot(y_train, 10)
y_test = tf.one_hot(y_test, 10)

# MNIST data image of shape 28 * 28 = 784
X = tf.placeholder(tf.float32, [None, 784])
# 0-9 digits recognition = 10 classes
Y = tf.placeholder(tf.float32, [None, 10])

W = tf.Variable(tf.random.normal([784, 10]))
b = tf.Variable(tf.random.normal([10]))

# Hypothesis (using softmax)
hypothesis = tf.nn.softmax(tf.matmul(X, W) + b)
cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.math.log(hypothesis), axis=1))
train = tf.compat.v1.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

# Test model
is_correct = tf.equal(tf.argmax(hypothesis, 1), tf.argmax(Y, 1))

# Calculate accuracy
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))

# Create a TensorFlow session
with tf.compat.v1.Session() as sess:
    # Initialize TensorFlow variables
    sess.run(tf.compat.v1.global_variables_initializer())

    # Training cycle
    num_epochs = 15
    batch_size = 100
    num_iterations = x_train.shape[0] // batch_size

    for epoch in range(num_epochs):
        avg_cost = 0
        for i in range(num_iterations):
            batch_xs = x_train[i * batch_size : (i + 1) * batch_size].reshape(-1, 784)
            batch_ys = y_train[i * batch_size : (i + 1) * batch_size].eval(session=tf.compat.v1.Session())
            _, cost_val = sess.run([train, cost], feed_dict={X: batch_xs, Y: batch_ys})
            avg_cost += cost_val / num_iterations
        print("Epoch: {:04d}, Cost: {:.9f}".format(epoch + 1, avg_cost))

    print("Learning finished")

    # Test the model using test sets
    test_accuracy = accuracy.eval(session=sess, feed_dict={X: x_test.reshape(-1, 784), Y: y_test.eval(session=tf.compat.v1.Session())})
    print("Accuracy: ", test_accuracy)

    # Get one and predict
    r = random.randint(0, x_test.shape[0] - 1)

    print("Label: ", sess.run(tf.argmax(y_test[r], 0)))
    print("Prediction: ", sess.run(tf.argmax(hypothesis, 1), feed_dict={X: x_test[r].reshape(-1, 784)}))
    plt.imshow(x_test[r], cmap="gray")
    plt.show()
