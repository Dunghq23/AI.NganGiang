import tensorflow as tf
import random
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist

tf.compat.v1.disable_eager_execution()

tf.compat.v1.set_random_seed(777)  # reproducibility

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Flatten the images from 28x28 to 784
x_train = x_train.reshape((-1, 784))
x_test = x_test.reshape((-1, 784))

# Convert labels to one-hot encoding
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

# Parameters
learning_rate = 0.001
training_epochs = 15
batch_size = 100

# Input placeholders
X = tf.compat.v1.placeholder(tf.float32, [None, 784])
Y = tf.compat.v1.placeholder(tf.float32, [None, 10])

# Weights and biases for NN layers with Xavier initialization
initializer = tf.initializers.GlorotUniform()

W1 = tf.Variable(initializer(shape=[784, 256]))
b1 = tf.Variable(tf.random.normal([256]))
L1 = tf.nn.relu(tf.matmul(X, W1) + b1)

W2 = tf.Variable(initializer(shape=[256, 256]))
b2 = tf.Variable(tf.random.normal([256]))
L2 = tf.nn.relu(tf.matmul(L1, W2) + b2)

W3 = tf.Variable(initializer(shape=[256, 10]))
b3 = tf.Variable(tf.random.normal([10]))
hypothesis = tf.matmul(L2, W3) + b3

# Define cost/loss and optimizer
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=hypothesis, labels=Y))
optimizer = tf.compat.v1.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

# Initialize
sess = tf.compat.v1.Session()
sess.run(tf.compat.v1.global_variables_initializer())

# Train the model
for epoch in range(training_epochs):
    avg_cost = 0
    total_batch = int(len(x_train) / batch_size)

    for i in range(total_batch):
        start = i * batch_size
        end = (i + 1) * batch_size
        batch_xs, batch_ys = x_train[start:end], y_train[start:end]
        feed_dict = {X: batch_xs, Y: batch_ys}
        c, _ = sess.run([cost, optimizer], feed_dict=feed_dict)
        avg_cost += c / total_batch

    print('Epoch:', '%04d' % (epoch + 1), 'cost = ', '{:.9f}'.format(avg_cost))

print('Learning Finished')

# Test the model and check accuracy
correct_prediction = tf.equal(tf.argmax(hypothesis, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print('Accuracy:', sess.run(accuracy, feed_dict={X: x_test, Y: y_test}))

# Get a random example and print label and prediction
r = random.randint(0, len(x_test) - 1)
label = y_test[r]
prediction = sess.run(tf.argmax(hypothesis, 1), feed_dict={X: x_test[r].reshape(1, -1)})

print("Label: ", sess.run(tf.argmax(label, 0)))
print("Prediction: ", prediction[0])

# Display the image
plt.imshow(x_test[r].reshape(28, 28), cmap="gray")
plt.show()