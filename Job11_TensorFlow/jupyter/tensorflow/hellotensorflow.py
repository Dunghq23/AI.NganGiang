import tensorflow.compat.v1 as tf


tf.disable_v2_behavior()
sess = tf.Session()
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b
print(sess.run(adder_node, feed_dict={a:2, b:1.5}))
print(sess.run(adder_node, feed_dict={a:[2, 3], b:[1, 4]}))

# ---------------------------------------------------------------------------------------
# Hãy cùng viết một biểu đồ tính toán đơn giản. Yếu tố cơ bản nhất là một hằng số. Các hàm Python xây dựng các hoạt động nhận các giá trị Tensor trong ứng dụng. Kết quả không yêu cầu đầu vào. Khi được thực hiện, nó sẽ in giá trị được truyền cho hàm tạo. Ở đây chúng ta tạo hai hằng số dấu phẩy động.
a = tf.constant(3.0, dtype=tf.float32)
b = tf.constant(4.0) # also tf.float32 implicitly
total = a + b
print(a)
print(b)
print(total)
# output":
    # Tensor("Const_16:0", shape=(), dtype=float32)
    # Tensor("Const_17:0", shape=(), dtype=float32)
    # Tensor("add_11:0", shape=(), dtype=float32)



# ---------------------------------------------------------------------------------------
sess = tf.Session()
print(sess.run(total))
# Output:
    # 7.0
    

# ---------------------------------------------------------------------------------------
# Có thể truyền nhiều tensor cho tf.Session.run Phương thức thự thi xử lý rõ ràng tất cả các kết hợp của bộ dữ liệu hoặc từ điển, như trong ví dụ sau:
print(sess.run({'ab': (a, b), 'total': total}))
# Output:
    # {'ab': (3.0, 4.0), 'total': 7.0}


# ---------------------------------------------------------------------------------------
import numpy as np
# Trong khi chạy tf.Session.run, tf.Tensor chỉ có một giá trị. Ví dụ: đoạn mã sau tạo ra một tf.Tensor gọi tf.random_uniform để tạo ra một vectơ ba phần tử tùy ý (với các giá trị trong [0,1]).

# Tạo mảng NumPy
array1 = np.array([1.8840756, 1.87149239, 1.84057522], dtype=np.float32)
array2 = np.array([2.8840756, 2.87149239, 2.84057522], dtype=np.float32)

# Bắt đầu một phiên TensorFlow
with tf.Session() as sess:
    # Chuyển đổi mảng NumPy thành tensor
    tensor1 = tf.constant(array1)
    tensor2 = tf.constant(array2)

    # In tensor trong phiên TensorFlow
    print("Tensor 1:")
    print(sess.run(tensor1))

    print("Tensor 2:")
    print(sess.run(tensor2))
# Output
    # Tensor 1:
    # [1.8840756 1.8714924 1.8405752]
    # Tensor 2:
    # [2.8840756 2.8714924 2.8405752]