
# Importing the required Keras modules containing model and layers
import tensorflow as tf
from tensorflow.keras import layers, models
import random

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Reshaping the array to 4-dims so that it can work with the Keras API
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
input_shape = (28, 28, 1)

# Making sure that the values are float so that we can get decimal points after division
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# Normalizing the RGB codes by dividing it to the max RGB value.
x_train /= 255
x_test /= 255
print('x_train shape:', x_train.shape)
print('Number of images in x_train', x_train.shape[0])
print('Number of images in x_test', x_test.shape[0])

# Create a sequential model
model = models.Sequential()

# -------------- Cấu trúc tầng mạng --------------
# Lớp Convolutional Đầu Tiên
model.add(layers.Conv2D(28, kernel_size=(3, 3), input_shape=input_shape))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))

# Lớp Fully Connected (1)
model.add(layers.Flatten())
model.add(layers.Dense(128, activation=tf.nn.relu))
model.add(layers.Dropout(0.2))

# Lớp Fully Connected (2)
model.add(layers.Dense(10, activation=tf.nn.softmax))
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Custom callback to format output
class CustomCallback(tf.keras.callbacks.Callback):
    def on_epoch_begin(self, epoch, logs=None):
        print(f'Epoch {epoch + 1}', end=' ')

    def on_epoch_end(self, epoch, logs=None):
        print(f'- loss: {logs["loss"]:.4f} - accuracy: {logs["accuracy"]:.4f}')

# Create an instance of the custom callback
custom_callback = CustomCallback()

# Fit the model with the custom callback
model.fit(x=x_train, y=y_train, epochs=15, callbacks=[custom_callback], verbose=0)

# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)

# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")

# Tải mô hình đã lưu
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = tf.keras.models.model_from_json(loaded_model_json)

# Tải trọng số vào mô hình đã tải
loaded_model.load_weights("model.h5")

# Biên soạn lại mô hình đã tải
loaded_model.compile(optimizer='adam',
                     loss='sparse_categorical_crossentropy',
                     metrics=['accuracy'])

# Chuẩn bị dữ liệu kiểm thử
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
x_test = x_test.astype('float32') / 255

# Đánh giá mô hình trên dữ liệu kiểm thử
accuracy = loaded_model.evaluate(x_test, y_test, verbose=0)[1]
print('Accuracy: {:.2%}'.format(accuracy))

# Lấy một ví dụ ngẫu nhiên và in ra nhãn thực tế và nhãn dự đoán
random_index = random.randint(0, len(x_test) - 1)
label = y_test[random_index]
prediction = loaded_model.predict(x_test[random_index].reshape(1, 28, 28, 1))
predicted_label = tf.argmax(prediction, 1).numpy()[0]

print("Label: ", label)
print("Prediction: ", predicted_label)