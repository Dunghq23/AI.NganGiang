**Google Vision API**

|Bước 1|<p>Truy cập Google Cloud để có thể lấy được API.</p><p><https://console.cloud.google.com></p><p>![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.001.png)</p><p>Lưu ý: Cần chọn vào Start Free( Bắt đầu dùng thử), thêm thông tin thanh toán. Thêm thẻ visa. Khi thành công hệ thống sẽ trừ tài khoản 1$ và sẽ hoàn lại ngay sau đó</p>|
| :-: | :- |
|Bước 2|<p>Nhấp chọn vào **Google Vision API** như hình bên dưới</p><p>![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.002.png)</p><p>Rồi nhấp chọn vào **New project**</p><p>![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.003.png)</p><p>Đặt tên cho project rồi nhấn **CREATE**</p><p>![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.004.png)</p>|
|Bước 3|<p>Tại bảng APIs, nhấp chọn vào **Go to APIs overview**</p><p>![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.005.png)</p><p>Tiếp tục nhấp chọn **ENABLE APIS AND SERVICES**</p><p>![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.006.png)</p><p>Tìm kiếm **Vision** trên thanh tìm kiếm</p><p>![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.007.png)</p><p>Và chọn vào **Cloud Vision API** như hình bên dưới</p><p>![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.008.png)</p><p></p>|
|Bước 3|<p>Sau khi API được bật, chọn **Credentials** như hình bên dưới</p><p>![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.009.png)</p><p>Tiếp tục nhấp chọn **CREATE CREDENTIAL**s để tạo mới thông tin xác thực</p><p>![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.010.png)</p><p>Tiếp theo chọn **Service account** như hình bên dưới</p><p>![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.011.png)</p><p>Đặt tên rồi tiếp tục nhấn **Create** và **Continue** rồi **Done** đến khi hoàn thành</p><p>![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.012.png)</p>|
|Bước 4|<p>Nhấn vào tên service account vừa tạo</p><p>![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.013.png)</p><p>Chọn vào **KEY** và nhấp vào **ADD KEY**</p><p>![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.014.png)</p><p>Tiếp tục nhấp vào **Create new key**</p><p>![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.015.png)</p><p>Chọn JSON, 1 file JSON sẽ tự động được tải xuống (*Lưu ý: cần đặt file này ở thư mục của dự án)*.</p><p>Nên đặt lại tên file để dễ hiểu và sử dụng.</p>|

**Cài đặt các gói cần thiết**

|Bước 1|Tạo thư mục **GoogleVisionAPI**|
| :- | :- |
|Bước 2|Chuyển file JSON đã tải về ở phần trước vào thư mục **GoogleVisionAPI**|
|Bước 3|<p>Đi vào trong thư mục **GoogleVisionAPI**</p><p>![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.016.png)</p>|
|Bước 4|<p>Cài thư viện google-cloud-vision bằng câu lệnh: **pip install google-cloud-vision**</p><p>![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.017.png)</p>|
|Bước 5|<p>Cài thư viện pandas bằng câu lệnh: **pip install pandas**</p><p>![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.018.png)</p>|



**Giải thích chi tiết code**

1. **Import các thư viện**

![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.019.png)

- **os, io**: Thư viện hỗ trợ quản lý hệ thống tệp tin và đọc/ghi dữ liệu dưới dạng luồng (stream).
- **google.cloud.vision\_v1**: Thư viện Google Cloud Vision API cho việc xử lý hình ảnh và nhận diện văn bản.
- **pandas as pd**: Thư viện để làm việc với dữ liệu dạng bảng.
- **tkinter as tk**: Thư viện để tạo giao diện đồ họa.
- **from tkinter import filedialog, messagebox**: Import các hàm từ thư viện tkinter cho hộp thoại chọn tệp và thông báo.

Chi tiết code tại đây:

|<p>import os, io</p><p>from google.cloud import vision\_v1</p><p>from google.cloud.vision\_v1 import types</p><p>import pandas as pd</p><p>import tkinter as tk</p><p>from tkinter import filedialog, messagebox</p>|
| :- |

1. **Đặt biến môi trường**

![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.020.png)

Câu lệnh trên được sử dụng để thiết lập biến môi trường **GOOGLE\_APPLICATION\_CREDENTIALS** trong môi trường thực thi của chương trình.

Giải thích chi tiết hơn:

- **os.environ** là một từ điển chứa các biến của môi trường hệ thống
- **['GOOGLE\_APPLICATION\_CREDENTIALS']**: Đây là cách truy cập hoặc thiết lập giá trị của biến môi trường cụ thể trong từ điển **os.environ**
- **ServiceAccToken\_ChuThang.json** Đây là giá trị mà biến môi trường  **['GOOGLE\_APPLICATION\_CREDENTIALS']** sẽ được thết lập thành. Trong trường hợp này, giá trị là một đường dẫn đến tệp JSON (tệp này được tải về tự động  sau khi hoàn thành bước 4 của cách hướng dẫn dùng GGAPI ở phía trên)

Khi biến môi trường **['GOOGLE\_APPLICATION\_CREDENTIALS']** được thiết lập với giá trị của đường dẫn đến tệp JSON chứa thông tin xác thực, các thư viện và API của google cloud sẽ tự động sử dụng thông tin trong tệp JSON này để xác thực và cho phép ứng dụng truy cập vào các dịch vụ của google Cloud.

Chi tiết code tại dây: 

|os.environ['GOOGLE\_APPLICATION\_CREDENTIALS'] = r'ServiceAccToken\_ChuThang.json'|
| :- |

1. **Tạo đối tượng ImageAnnotatorClient**

![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.021.png)

Dòng mã này để tạo một đối tượng client, tương tác với dịch vụ Google Cloud Vision API

Giải thích chi tiết hơn:

- **client**: là tiên biến sử dụng để lưu trữ một đối tượng của lớp **ImageAnotatoClient** đã được import từ thư viện **google.cloud.vision\_v1**. Đối tượng nay sẽ là cầu nối giữa ứng dụng của mình và dịch vụ bên Google Vision API. Nó cung cấp các phương thức để gửi yêu cầu đến API và xử lý phản hồi từ API.

Chi tiết code tại đây:

|client = vision\_v1.ImageAnnotatorClient()|
| :- |

1. **Định nghĩa hàm detectText(FILE\_PATH)**

![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.022.png)

|Bước 1|<p>Mở và đọc tệp hình ảnh</p><p>![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.023.png)</p><p>- Sử dụng **io.open** để mở tệp hình ảnh được truyền vào (**FILE\_PATH**) ở chế độ đọc nhị phân (‘**rb’**)</p><p>- Nội dung của tệp được vào biến **content**. Đây là dữ liệu nhị phân của hình ảnh.</p>|
| :-: | :- |
|Bước 2|<p>Tạo đối tượng hình ảnh </p><p>![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.024.png)</p><p>- Đối tượng **Image** được tạo bằng cách cung cấp nội dung của hình ảnh content cho thuộc tính content.</p>|
|Bước 3|<p>Gửi yêu cầu nhận diện văn bản đến dịch vụ Vision API chứa thông tin về văn bản đã được nhận diện</p><p>![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.025.png)</p><p>- Hàm text\_detection của đối tượng client (ImageAnnotatorClient) được gọi để gửi yêu cầu nhận diện văn bản bằng cách sử dụng đối tượng hình ảnh đã được tạo.</p>|
|Bước 4|<p>Trích xuất thông tin văn bản từ phản hồi</p><p>![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.026.png)</p><p>- Kết quả được phản hồi từ dịch vụ Vision API chứa thông tin về văn bản đã được nhận diện và sẽ được lưu vào biến **texts**</p>|
|Bước 5|<p>Xử lý thông tin văn bản</p><p>![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.027.png)</p><p>- Tạo từ diển **data** để lưu trữ thông tin như ngôn ngữ (**locale**) và nội dung văn bản (**description**) của mỗi phần văn bản trong danh sách **texts**</p><p>- Dùng vòng lặp for để duyệt qua danh sách **texts** và trích xuất thông tin cần thiết vào từ điển **data**.</p>|
|Bước 6|<p>Tạo DataFrame từ thông tin văn bản</p><p>![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.028.png)</p><p>- Sau khi thu thập thông tin từ danh sách **texts**, dữ liệu được chuyển vào một DataFrame Pandas để dễ dàng xử lý và truy vấn</p>|
|Bước 7|<p>Lấy nội dung từ văn bản</p><p>![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.029.png)</p><p>- Biến **texts** được gán bằng nội dung văn bản đầu tiên trong DataFrame, tức là phần văn bản đầu tiên được nhận diện từ hình ảnh</p>|
|Bước 8|<p>Hiển thị kết quả</p><p>![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.030.png)</p><p>- Nội dung văn bản nhận diện được in ra màn hình console thông qua **print**.</p><p>- Hộp thoại thông báo (**messagebox.showinfo**) được sử dụng để hiển thị nội dung văn bản nhận diện ra giao diện đồ họa với tiêu đề "Kết quả".</p>|

Chi tiết code tại đây:

|<p>def detectText(FILE\_PATH):</p><p>`    `with io.open(FILE\_PATH, 'rb') as image\_file:</p><p>`        `content = image\_file.read()</p><p></p><p>`    `image = vision\_v1.types.Image(content=content)</p><p>`    `response = client.text\_detection(image=image)</p><p>`    `texts = response.text\_annotations</p><p></p><p>`    `data = {'locale': [], 'description': []}</p><p>`    `for text in texts:</p><p>`        `data['locale'].append(text.locale)</p><p>`        `data['description'].append(text.description)</p><p>`    `df = pd.DataFrame(data)</p><p>`    `texts = df['description'][0]</p><p>`    `print(texts)</p><p>`    `messagebox.showinfo("Kết quả", texts)</p>|
| :- |

1. **Định nghĩa hàm open\_and\_detect()**

![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.031.png)

|Bước 1|<p>![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.032.png)</p><p>Câu lệnh này sẽ khiến hộp thoại file được bật lên và cho phép người dùng chọn file ảnh  (Chỉ nhận các định dạng file .jpg .jpeg .png .gif .bmp) và ảnh được chọn sẽ có đường dẫn được lưu vào biến **file\_path**</p>|
| :-: | :- |
|Bước 2|<p>![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.033.png)</p><p>Nếu file ảnh được chọn đúng định dạng, đường dẫn sẽ được in ra trong terminal và sau đó chương trình sẽ gọi tới hàm **detectText(file\_path)**</p>|

Chi tiết code tại đây:

|<p>def open\_and\_detect():</p><p>`    `file\_path = filedialog.askopenfilename(filetypes=[("Image files", "\*.jpg \*.jpeg \*.png \*.gif \*.bmp")])</p><p>`    `if file\_path:</p><p>`        `print('Đường dẫn:', file\_path)</p><p>`        `detectText(file\_path)</p>|
| :- |

**

1. **Tạo giao diện đồ họa với Tkinter**

![](Aspose.Words.3672c6ec-c0a6-4271-a129-b0b983e50480.034.png)

Mã nguồn tạo một cửa sổ giao diện đồ họa sử dụng Tkinter và một nút "Chọn ảnh". Khi người dùng nhấn vào nút này, ứng dụng sẽ bắt đầu quá trình nhận diện văn bản từ hình ảnh. Chi tiết của mã:

**root = tk.Tk()**: Tạo cửa sổ giao diện đồ họa.

**root.geometry("400x400")**: Đặt kích thước cửa sổ là 400x400 pixel.

**root.title("App nhận diện khuôn mặt qua ảnh")**: Đặt tiêu đề cho cửa sổ.

**open\_button = tk.Button(root, text="Chọn ảnh", command=open\_and\_detect)**: Tạo nút "Chọn ảnh" và liên kết nó với hàm open\_and\_detect.

**open\_button.pack(pady=30)**: Đặt nút vào cửa sổ và đặt khoảng cách dưới nút là 30 pixel.

**root.mainloop()**: Khởi chạy giao diện và chờ sự tương tác từ người dùng.

Chi tiết code tại đây:

|<p>root = tk.Tk()</p><p>root.geometry("400x400")</p><p>root.title("App nhận diện khuôn mặt qua ảnh")</p><p>open\_button = tk.Button(root, text="Chọn ảnh", command=open\_and\_detect)</p><p>open\_button.pack(pady=30)</p><p>root.mainloop()</p>|
| :- |



**CODE ĐẦY ĐỦ**

|<p>import os, io</p><p>from google.cloud import vision\_v1</p><p>from google.cloud.vision\_v1 import types</p><p>import pandas as pd</p><p>import tkinter as tk</p><p>from tkinter import filedialog, messagebox</p><p></p><p>os.environ['GOOGLE\_APPLICATION\_CREDENTIALS'] = r'ServiceAccToken\_ChuThang.json'</p><p>client = vision\_v1.ImageAnnotatorClient()</p><p></p><p>def detectText(FILE\_PATH):</p><p>`    `with io.open(FILE\_PATH, 'rb') as image\_file:</p><p>`        `content = image\_file.read()</p><p></p><p>`    `image = vision\_v1.types.Image(content=content)</p><p>`    `response = client.text\_detection(image=image)</p><p>`    `texts = response.text\_annotations</p><p></p><p>`    `data = {'locale': [], 'description': []}</p><p>`    `for text in texts:</p><p>`        `data['locale'].append(text.locale)</p><p>`        `data['description'].append(text.description)</p><p>`    `df = pd.DataFrame(data)</p><p>`    `texts = df['description'][0]</p><p>`    `print(texts)</p><p>`    `messagebox.showinfo("Kết quả", texts)</p><p></p><p># Hàm xử lý sự kiện người dùng nhấn nút "Chọn ảnh"</p><p>def open\_and\_detect():</p><p>`    `file\_path = filedialog.askopenfilename(filetypes=[("Image files", "\*.jpg \*.jpeg \*.png \*.gif \*.bmp")])</p><p>`    `if file\_path:</p><p>`        `print('Đường dẫn:', file\_path)</p><p>`        `detectText(file\_path)</p><p></p><p># ======================= Giao diện đồ họa ====================</p><p># Tạo cửa sổ GDDH</p><p>root = tk.Tk()</p><p>root.geometry("400x400")</p><p>root.title("App nhận diện chữ qua ảnh")</p><p># Tạo nút chọn tệp</p><p>open\_button = tk.Button(root, text="Chọn ảnh", command=open\_and\_detect)</p><p>open\_button.pack(pady=30)</p><p># Khởi chạy giao diện đồ họa</p><p>root.mainloop()</p>|
| :- |

