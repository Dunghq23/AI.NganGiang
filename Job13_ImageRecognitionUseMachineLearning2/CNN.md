# **BẢN GIẢI THÍCH CHƯƠNG TRÌNH XÂY DỰNG VÀ HUẤN LUYỆN TRÊN TẬP SỐ MNIST THÔNG QUA THUẬT TOÁN CNN**


## 1. **Import thư viện:**
   ```python
   import tensorflow as tf
   from tensorflow.keras import layers, models
   import random
   ```

   *  **`tensorflow`**:
      - Đây là lệnh import thư viện chính TensorFlow, một thư viện mã nguồn mở phổ biến được sử dụng để xây dựng và huấn luyện mô hình học máy.

   *  **`from tensorflow.keras import layers, models`**:
      - `from tensorflow.keras` là một module của TensorFlow chứa các công cụ và chức năng được mở rộng từ Keras, một thư viện cao cấp giúp đơn giản hóa quá trình xây dựng và huấn luyện mô hình học máy.
      - `layers` và `models` là hai module trong Keras được sử dụng để định nghĩa các lớp (layers) và mô hình (models) của mạng nơ-ron.

   *  **`random`**:
      - Lệnh import thư viện `random` giúp tạo ra các số ngẫu nhiên, và nó được sử dụng trong mã nguồn để chọn ngẫu nhiên một ví dụ từ tập kiểm thử.

## 2. **Tải và chuẩn bị dữ liệu:**
   ```python
   (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
   ```

   - Sử dụng hàm `load_data` của MNIST để tải dữ liệu huấn luyện và kiểm thử.

## 3. **Chuẩn bị dữ liệu đầu vào cho mô hình:**
   ```python
   x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
   x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
   ```

   - Reshape dữ liệu để phù hợp với đầu vào của mô hình convolutional (1 kênh màu).

## 4. **Chuẩn hóa dữ liệu:**
   ```python
   x_train = x_train.astype('float32') / 255
   x_test = x_test.astype('float32') / 255
   ```

   - Chuyển đổi kiểu dữ liệu sang float32 và chuẩn hóa giá trị về khoảng [0, 1].

## 5. **Xây dựng mô hình:**
   ```python
   model = models.Sequential()
   ```

   - Tạo một mô hình sequential.

   ```python
   model.add(layers.Conv2D(28, kernel_size=(3, 3), input_shape=input_shape))
   model.add(layers.MaxPooling2D(pool_size=(2, 2)))
   ```

   - Thêm một lớp convolutional và một lớp max pooling.

   ```python
   model.add(layers.Flatten())
   model.add(layers.Dense(128, activation=tf.nn.relu))
   model.add(layers.Dropout(0.2))
   ```

   - Flatten và thêm một lớp fully connected với ReLU activation và một lớp dropout.

   ```python
   model.add(layers.Dense(10, activation=tf.nn.softmax))
   ```

   - Thêm lớp fully connected cuối cùng với softmax activation.

   ```python
   model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
   ```

   - Compile mô hình với optimizer Adam, hàm loss sparse categorical crossentropy và theo dõi độ chính xác.

## 6. **Tạo callback và huấn luyện mô hình:**
   ```python
   class CustomCallback(tf.keras.callbacks.Callback):
       # ... (Xem mã nguồn để biết đầy đủ)

   custom_callback = CustomCallback()
   model.fit(x=x_train, y=y_train, epochs=15, callbacks=[custom_callback], verbose=0)
   ```

   - Tạo một callback tùy chỉnh để in thông tin theo dõi trong quá trình huấn luyện và sử dụng nó trong quá trình huấn luyện mô hình.

## 7. **Lưu mô hình và trọng số:**
   ```python
   model_json = model.to_json()
   with open("model.json", "w") as json_file:
       json_file.write(model_json)

   model.save_weights("model.h5")
   ```

   - Lưu cấu trúc mô hình vào file JSON và lưu trọng số vào file HDF5.

## 8. **Tải lại mô hình và trọng số:**
   ```python
   json_file = open('model.json', 'r')
   loaded_model_json = json_file.read()
   json_file.close()
   loaded_model = tf.keras.models.model_from_json(loaded_model_json)
   ```

   - Đọc file JSON để tạo lại cấu trúc mô hình và sau đó load trọng số từ file HDF5.

   ```python
   loaded_model.load_weights("model.h5")
   ```

   - Load trọng số vào mô hình đã tạo.

## 9. **Đánh giá mô hình trên dữ liệu kiểm thử:**
   ```python
   accuracy = loaded_model.evaluate(x_test, y_test, verbose=0)[1]
   print('Accuracy: {:.2%}'.format(accuracy))
   ```

   - Đánh giá độ chính xác của mô hình trên tập dữ liệu kiểm thử.

## 10. **Dự đoán và in ra kết quả:**
    ```python
    random_index = random.randint(0, len(x_test) - 1)
    label = y_test[random_index]
    prediction = loaded_model.predict(x_test[random_index].reshape(1, 28, 28, 1))
    predicted_label = tf.argmax(prediction, 1).numpy()[0]

    print("Label: ", label)
    print("Prediction: ", predicted_label)
    ```

    - Chọn một ví dụ ngẫu nhiên từ tập kiểm thử và in ra nhãn thực tế và nhãn dự đoán. 