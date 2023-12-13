# import tensorflow as tf
# import random
# import matplotlib.pyplot as plt
# from tensorflow.keras.datasets import mnist

# tf.random.set_seed(777)

# (x_train, y_train), (x_test, y_test) = mnist.load_data()
# x_train, x_test = x_train / 255.0, x_test / 255.0

# # parameters
# learning_rate = 0.001
# training_epochs = 15
# batch_size = 100

# # Tắt tính toán tự động
# tf.compat.v1.disable_eager_execution()

# # input place holders
# X = tf.compat.v1.placeholder(tf.float32, [None, 784])
# Y = tf.compat.v1.placeholder(tf.float32, [None, 10])

# # weights & bias for nn layers
# W1 = tf.Variable(tf.compat.v1.random_normal([784, 256]))
# b1 = tf.Variable(tf.compat.v1.random_normal([256]))
# L1 = tf.nn.relu(tf.matmul(X, W1) + b1)

# W2 = tf.Variable(tf.compat.v1.random_normal([256, 256]))
# b2 = tf.Variable(tf.compat.v1.random_normal([256]))
# L2 = tf.nn.relu(tf.matmul(L1, W2) + b2)

# W3 = tf.Variable(tf.compat.v1.random_normal([256, 10]))
# b3 = tf.Variable(tf.compat.v1.random_normal([10]))
# hypothesis = tf.matmul(L2, W3) + b3

# # define cost/loss & optimizer
# cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
#   logits=hypothesis, labels=Y
# ))
# optimizer = tf.compat.v1.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

# # initialize
# sess = tf.compat.v1.Session()
# sess.run(tf.compat.v1.global_variables_initializer())

# # train my model
# for epoch in range(training_epochs):
#     avg_cost = 0
#     total_batch = int(len(x_train) / batch_size)

#     for i in range(total_batch):
#         start = i * batch_size
#         end = (i + 1) * batch_size
#         batch_xs, batch_ys = x_train[start:end], y_train[start:end]
#         batch_xs = batch_xs.reshape(-1, 784)
#         batch_ys = tf.keras.utils.to_categorical(batch_ys, 10)
#         feed_dict = {X: batch_xs, Y: batch_ys}
#         c, _ = sess.run([cost, optimizer], feed_dict=feed_dict)
#         avg_cost += c / total_batch

#     print('Epoch:', '%04d' % (epoch + 1), 'cost = ', '{:.9f}'.format(avg_cost))

# print('Learning Finished')

# # Kiểm thử mô hình và kiểm tra độ chính xác
# correct_prediction = tf.equal(tf.argmax(hypothesis, 1), tf.argmax(Y, 1))
# accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
# print('Accuracy:', sess.run(accuracy, feed_dict={
#     X: x_test.reshape(-1, 784),
#     Y: tf.keras.utils.to_categorical(y_test, 10)
# }))

# # Lấy một ví dụ và dự đoán
# r = random.randint(0, len(x_test) - 1)
# print("Label:", y_test[r])
# print("Prediction:", sess.run(tf.argmax(hypothesis, 1), feed_dict={X: x_test[r].reshape(1, -1)}))
# plt.imshow(x_test[r], cmap="hot")
# plt.show()

