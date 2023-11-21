# **BẢN GIẢI THÍCH CHƯƠNG TRÌNH XÂY DỰNG VÀ HUẤN LUYỆN TRÊN TẬP SỐ MNIST THÔNG QUA THUẬT TOÁN CNN**

## 1. **Import thư viện:**

```python
import tensorflow as tf
from tensorflow.keras import layers, models
import random
```

- **`tensorflow`**:

  - Đây là lệnh import thư viện chính TensorFlow, một thư viện mã nguồn mở phổ biến được sử dụng để xây dựng và huấn luyện mô hình học máy.

- **`from tensorflow.keras import layers, models`**:

  - `from tensorflow.keras` là một module của TensorFlow chứa các công cụ và chức năng được mở rộng từ Keras, một thư viện cao cấp giúp đơn giản hóa quá trình xây dựng và huấn luyện mô hình học máy.
  - `layers` và `models` là hai module trong Keras được sử dụng để định nghĩa các lớp (layers) và mô hình (models) của mạng nơ-ron.

- **`random`**:
  - Lệnh import thư viện `random` giúp tạo ra các số ngẫu nhiên, và nó được sử dụng trong mã nguồn để chọn ngẫu nhiên một ví dụ từ tập kiểm thử.

## 2. **Tải và chuẩn bị dữ liệu:**

```python
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
```

Tải dữ liệu từ bộ dữ liệu MNIST vào bốn biến: `x_train`, `y_train`, `x_test`, và `y_test`. Dữ liệu MNIST là một bộ dữ liệu phổ biến trong lĩnh vực học máy, chứa hình ảnh của các chữ số từ 0 đến 9.

- `x_train`: Là tập dữ liệu huấn luyện chứa các hình ảnh của chữ số.
- `y_train`: Là nhãn tương ứng với từng hình ảnh trong tập huấn luyện, đại diện cho chữ số thực tế mà hình ảnh đó biểu diễn.
- `x_test`: Là tập dữ liệu kiểm thử, chứa các hình ảnh khác nhau so với tập huấn luyện.
- `y_test`: Là nhãn tương ứng với từng hình ảnh trong tập kiểm thử.

Hàm `load_data()` được cung cấp bởi Keras trong TensorFlow để thuận tiện việc tải dữ liệu MNIST mà không cần tải về thủ công. Khi dữ liệu đã được tải, các biến được gán giá trị từ kết quả trả về của hàm `load_data()`.

## 3. **Chuẩn bị dữ liệu đầu vào cho mô hình:**

```python
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
```

Đặt lại hình dạng của dữ liệu ảnh từ dạng ma trận 2D (28x28 pixel) thành dạng tensor 4D để phù hợp với đầu vào của mô hình convolutional trong framework Keras.

- `x_train` và `x_test` là hai biến chứa dữ liệu hình ảnh của tập huấn luyện và tập kiểm thử, lần lượt.
- `reshape` được sử dụng để thay đổi hình dạng của dữ liệu. Đối số `(x_train.shape[0], 28, 28, 1)` mô tả kích thước mới của dữ liệu.
  - `x_train.shape[0]`: Số lượng mẫu trong tập huấn luyện.
  - `28, 28`: Kích thước của mỗi ảnh (28x28 pixel).
  - `1`: Số kênh màu (1 trong trường hợp ảnh grayscale).

Do đó, sau dòng mã này, `x_train` và `x_test` trở thành các tensor 4D, thích hợp để sử dụng trong các mô hình mạng nơ-ron convolutional, với kích thước là `(số lượng mẫu, chiều cao, chiều rộng, số kênh màu)`.

## 4. **Chuẩn hóa dữ liệu:**

```python
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255
```

1. **Chuyển đổi kiểu dữ liệu:**

   - `x_train` và `x_test` ban đầu có kiểu dữ liệu là integer (số nguyên), thường là giá trị của các pixel trong ảnh (trong khoảng từ 0 đến 255). Để tiếp tục làm việc với mô hình học máy, đặc biệt là các mô hình sử dụng phép toán dấu chấm động (float), ta cần chuyển đổi chúng sang kiểu dữ liệu float32.

2. **Chuẩn hóa giá trị pixel:**
   - Sau khi chuyển đổi kiểu dữ liệu, các giá trị pixel trong `x_train` và `x_test` được chuẩn hóa bằng cách chia cho 255. Việc này đưa các giá trị pixel về khoảng từ 0 đến 1. Chuẩn hóa giúp mô hình học máy hội tụ nhanh hơn và giảm ảnh hưởng của sự chênh lệch lớn giữa các giá trị.

Kết quả là, `x_train` và `x_test` sau đoạn mã này là các tensor có kiểu dữ liệu float32 và giá trị nằm trong khoảng [0, 1], sẵn sàng được sử dụng để huấn luyện mô hình mạng nơ-ron convolutional.

## 5. **Xây dựng mô hình:**

Phần này xây dựng một mô hình mạng nơ-ron sử dụng framework Keras. Dưới đây là giải thích chi tiết từng bước:

1. **Tạo một mô hình sequential:**

   ```python
   model = models.Sequential()
   ```

   - Tạo một mô hình sequential, một loại mô hình trong Keras cho phép xây dựng mạng nơ-ron layer by layer theo thứ tự tuần tự.

2. **Thêm lớp convolutional và lớp max pooling:**

   ```python
   model.add(layers.Conv2D(28, kernel_size=(3, 3), input_shape=input_shape))
   model.add(layers.MaxPooling2D(pool_size=(2, 2)))
   ```

   - Thêm một lớp convolutional với 28 bộ lọc kích thước (3, 3) và input_shape là kích thước của mỗi ảnh (28, 28, 1).
   - Thêm một lớp max pooling với pool_size là (2, 2) để giảm kích thước của đầu ra.

3. **Flatten và thêm lớp fully connected:**

   ```python
   model.add(layers.Flatten())
   model.add(layers.Dense(128, activation=tf.nn.relu))
   model.add(layers.Dropout(0.2))
   ```

   - Thêm lớp Flatten để chuyển từ tensor 3D (sau lớp convolutional và max pooling) sang vector 1D.
   - Thêm một lớp fully connected (dense) với 128 nơ-ron và activation ReLU.
   - Thêm một lớp dropout với tỷ lệ dropout là 0.2 để giảm nguy cơ overfitting.

4. **Thêm lớp fully connected cuối cùng:**

   ```python
   model.add(layers.Dense(10, activation=tf.nn.softmax))
   ```

   - Thêm lớp fully connected cuối cùng với 10 nơ-ron (do MNIST có 10 lớp) và activation là softmax để chuyển đầu ra thành các xác suất.

5. **Compile mô hình:**
   ```python
   model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
   ```
   - Compile mô hình với optimizer là 'adam', một thuật toán tối ưu hóa thường được sử dụng.
   - Loss function được chọn là 'sparse_categorical_crossentropy', phù hợp cho bài toán phân loại với nhiều lớp và nhãn không cần được mã hóa one-hot.
   - Theo dõi độ chính xác trong quá trình huấn luyện.

## 6. **Tạo callback và huấn luyện mô hình:**

Phần này tạo và sử dụng một callback tùy chỉnh trong quá trình huấn luyện mô hình để theo dõi và hiển thị thông tin sau mỗi epoch. Dưới đây là giải thích chi tiết:

1. **Custom Callback:**

   ```python
   class CustomCallback(tf.keras.callbacks.Callback):
       def on_epoch_begin(self, epoch, logs=None):
           print(f'Epoch {epoch + 1}', end=' ')

       def on_epoch_end(self, epoch, logs=None):
           print(f'- loss: {logs["loss"]:.4f} - accuracy: {logs["accuracy"]:.4f}')
   ```

   - Định nghĩa một lớp `CustomCallback` kế thừa từ `tf.keras.callbacks.Callback`.
   - Cung cấp hai hàm `on_epoch_begin` và `on_epoch_end` để in ra thông tin tùy chỉnh ở đầu và cuối mỗi epoch.

2. **Tạo một instance của callback tùy chỉnh:**

   ```python
   custom_callback = CustomCallback()
   ```

   - Tạo một đối tượng của lớp `CustomCallback` để sử dụng trong quá trình huấn luyện.

3. **Fit the model with the custom callback:**
   ```python
   model.fit(x=x_train, y=y_train, epochs=15, callbacks=[custom_callback], verbose=0)
   ```
   - Sử dụng phương thức `fit` để huấn luyện mô hình.
   - Truyền vào danh sách callbacks với callback tùy chỉnh đã tạo để theo dõi và hiển thị thông tin trong quá trình huấn luyện.
   - Tham số `verbose=0` để tắt việc hiển thị thông tin tiến trình trong quá trình huấn luyện. Thông tin sẽ được hiển thị bởi callback tùy chỉnh.

## 7. **Lưu mô hình và trọng số:**

Phần này thực hiện việc lưu cấu trúc mô hình và trọng số của mô hình sau khi đã huấn luyện vào các tệp tin. Dưới đây là giải thích chi tiết:

1. **Serialize model to JSON:**

   ```python
   model_json = model.to_json()
   with open("model.json", "w") as json_file:
       json_file.write(model_json)
   ```

   - Sử dụng phương thức `to_json()` của mô hình để chuyển đổi cấu trúc của mô hình thành định dạng JSON.
   - Mở một tệp tin `"model.json"` ở chế độ ghi và ghi nội dung JSON của mô hình vào tệp tin.

2. **Serialize weights to HDF5:**

   ```python
   model.save_weights("model.h5")
   ```

   - Sử dụng phương thức `save_weights` của mô hình để lưu trọng số của mô hình vào một tệp tin HDF5 (Hierarchical Data Format version 5). Định dạng này thích hợp cho việc lưu trữ trọng số mô hình.
   - Tệp tin HDF5 được đặt tên là `"model.h5"`.

3. **Print a confirmation message:**
   ```python
   print("Saved model to disk")
   ```
   - In ra một thông báo xác nhận để cho biết rằng cả cấu trúc mô hình và trọng số đã được lưu thành công vào các tệp tin.

Kết quả, sau khi chạy phần này, bạn sẽ có một tệp tin `"model.json"` chứa cấu trúc của mô hình và một tệp tin `"model.h5"` chứa trọng số của mô hình. Điều này cho phép bạn sau này có thể tái tạo lại mô hình và sử dụng nó mà không cần phải huấn luyện lại từ đầu.

## 8. **Tải lại mô hình và trọng số:**

Phần này thực hiện việc tải lại cấu trúc mô hình và trọng số từ các tệp tin đã lưu. Dưới đây là giải thích chi tiết:

1. **Tải cấu trúc mô hình từ file JSON:**

   ```python
   json_file = open('model.json', 'r')
   loaded_model_json = json_file.read()
   json_file.close()
   loaded_model = tf.keras.models.model_from_json(loaded_model_json)
   ```

   - Mở tệp tin `"model.json"` ở chế độ đọc (`'r'`) và đọc nội dung của nó vào biến `loaded_model_json`.
   - Đóng tệp tin sau khi đã đọc xong.
   - Sử dụng `tf.keras.models.model_from_json` để tạo một mô hình mới từ cấu trúc mô hình đã được lưu.

2. **Tải trọng số vào mô hình đã tải:**
   ```python
   loaded_model.load_weights("model.h5")
   ```
   - Sử dụng phương thức `load_weights` của mô hình đã tải để tải trọng số từ tệp tin `"model.h5"` vào mô hình.

Kết quả của phần này là bạn có một mô hình (`loaded_model`) có cấu trúc và trọng số giống hệt như mô hình đã được lưu trước đó. Bạn có thể sử dụng mô hình này để thực hiện dự đoán trên dữ liệu mới mà không cần phải huấn luyện lại từ đầu.

## 9. **Biên soạn lại mô hình đã tải, chuẩn bị dữ liệu kiểm thử:**

1. **Biên soạn lại mô hình đã tải:**

   ```python
   loaded_model.compile(optimizer='adam',
                        loss='sparse_categorical_crossentropy',
                        metrics=['accuracy'])
   ```

   - Sử dụng phương thức `compile` để biên soạn lại mô hình đã tải.
   - Chọn optimizer là 'adam', loss function là 'sparse_categorical_crossentropy' (phù hợp cho bài toán phân loại với nhãn không được mã hóa one-hot), và theo dõi độ chính xác.

2. **Chuẩn bị dữ liệu kiểm thử:**
   ```python
   (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
   x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
   x_test = x_test.astype('float32') / 255
   ```
   - Tải lại dữ liệu kiểm thử từ bộ dữ liệu MNIST.
   - Reshape dữ liệu kiểm thử để phù hợp với đầu vào của mô hình (có 1 kênh màu).
   - Chuyển đổi kiểu dữ liệu về float32 và chuẩn hóa giá trị pixel về khoảng [0, 1].

## 10. **Đánh giá mô hình trên dữ liệu kiểm thử:**

Phần này đánh giá mô hình trên dữ liệu kiểm thử và in ra độ chính xác. Dưới đây là giải thích chi tiết:

1. **Đánh giá mô hình trên dữ liệu kiểm thử:**

   ```python
   accuracy = loaded_model.evaluate(x_test, y_test, verbose=0)[1]
   ```

   - Sử dụng phương thức `evaluate` của mô hình để đánh giá hiệu suất của mô hình trên dữ liệu kiểm thử.
   - `x_test`: Dữ liệu kiểm thử.
   - `y_test`: Nhãn tương ứng với dữ liệu kiểm thử.
   - `verbose=0`: Tắt việc hiển thị thông tin tiến trình trong quá trình đánh giá.
   - Kết quả của hàm `evaluate` là một danh sách các giá trị mất mát và các metric đã được đặt trong quá trình biên soạn lại mô hình. Trong trường hợp này, `accuracy` được chọn làm metric chính.

2. **In ra độ chính xác:**
   ```python
   print('Accuracy: {:.2%}'.format(accuracy))
   ```
   - In ra độ chính xác của mô hình trên dữ liệu kiểm thử dưới dạng phần trăm (có hai chữ số thập phân).

## 11. **Dự đoán và in ra kết quả:**

1. **Chọn một ví dụ ngẫu nhiên:**

   ```python
   random_index = random.randint(0, len(x_test) - 1)
   label = y_test[random_index]
   ```

   - Sử dụng thư viện `random` để chọn ngẫu nhiên một chỉ mục từ tập dữ liệu kiểm thử.
   - Lấy nhãn thực tế (`label`) của ví dụ được chọn.

2. **Thực hiện dự đoán và lấy nhãn dự đoán:**

   ```python
   prediction = loaded_model.predict(x_test[random_index].reshape(1, 28, 28, 1))
   predicted_label = tf.argmax(prediction, 1).numpy()[0]
   ```

   - Sử dụng mô hình đã tải để dự đoán nhãn của ví dụ đã chọn.
   - `x_test[random_index]`: Lấy dữ liệu của ví dụ ngẫu nhiên.
   - `.reshape(1, 28, 28, 1)`: Đảm bảo rằng dữ liệu có hình dạng phù hợp với đầu vào của mô hình.
   - `tf.argmax(prediction, 1).numpy()[0]`: Chọn nhãn có xác suất cao nhất từ đầu ra dự đoán của mô hình.

3. **In ra nhãn thực tế và nhãn dự đoán:**
   ```python
   print("Label: ", label)
   print("Prediction: ", predicted_label)
   ```
   - In ra nhãn thực tế và nhãn dự đoán.

Kết quả là bạn sẽ có thông tin về một ví dụ ngẫu nhiên, nhãn thực tế và nhãn dự đoán của mô hình cho ví dụ đó.
