import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.datasets import mnist
import random
import matplotlib.pyplot as plt

tf.random.set_seed(777)  # Reproducibility

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize pixel values to be between 0 and 1
x_train, x_test = x_train / 255.0, x_test / 255.0

# Flatten the images
x_train_flat = x_train.reshape((x_train.shape[0], -1))
x_test_flat = x_test.reshape((x_test.shape[0], -1))

# Convert labels to one-hot encoding
y_train = tf.one_hot(y_train, 10)
y_test = tf.one_hot(y_test, 10)

# Parameters
learning_rate = 0.001
training_epochs = 15
batch_size = 100

# Input placeholders
X = Input(shape=(784,))

# Define the model
L1 = Dense(512, activation='relu')(X)
L1_dropout = Dropout(0.3)(L1)

L2 = Dense(512, activation='relu')(L1_dropout)
L2_dropout = Dropout(0.3)(L2)

L3 = Dense(512, activation='relu')(L2_dropout)
L3_dropout = Dropout(0.3)(L3)

L4 = Dense(512, activation='relu')(L3_dropout)
L4_dropout = Dropout(0.3)(L4)

hypothesis = Dense(10, activation='softmax')(L4_dropout)

# Build the model
model = Model(inputs=X, outputs=hypothesis)

# Compile the model
optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)
model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

# Custom training loop
for epoch in range(training_epochs):
    avg_cost = 0
    total_batch = int(len(x_train) / batch_size)

    for i in range(total_batch):
        start = i * batch_size
        end = (i + 1) * batch_size
        batch_xs, batch_ys = x_train_flat[start:end], y_train[start:end]

        with tf.GradientTape() as tape:
            logits = model(batch_xs, training=True)
            loss = tf.keras.losses.categorical_crossentropy(batch_ys, logits)
            avg_cost += tf.reduce_mean(loss) / total_batch

        gradients = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(gradients, model.trainable_variables))

    print('Epoch:', '{:04d}'.format(epoch + 1), 'cost = ', '{:.9f}'.format(avg_cost))

print('Learning Finished')

# Test the model and check accuracy
accuracy = model.evaluate(x_test_flat, y_test, batch_size=batch_size, verbose=0)[1]
print('Accuracy:', accuracy)

# Get a random example and print label and prediction
r = random.randint(0, len(x_test) - 1)
label = y_test[r]
prediction = model.predict(x_test_flat[r].reshape(1, -1))
predicted_label = tf.argmax(prediction, 1).numpy()[0]

print("Label: ", tf.argmax(label, 0).numpy())
print("Prediction: ", predicted_label)

# Display the image
plt.imshow(x_test[r].reshape(28, 28), cmap="gray")
plt.show()
