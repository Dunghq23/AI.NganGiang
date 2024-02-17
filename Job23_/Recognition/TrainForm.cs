using AForge.Video.DirectShow;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;


using AForge.Video.DirectShow;
using AForge.Video;
using System.Threading;

namespace Recognition
{
    public partial class TrainForm : Form
    {
        private string selectedFilePathTrain = null;
        private string selectedFilePathRecognize = null;
        private string pythonExePath = @"C:/Users/Admin/AppData/Local/Microsoft/WindowsApps/python3.12.exe";
        string pythonScriptPath = @"../../python/main.py";
        string currentDirectory = Environment.CurrentDirectory;
        private string tempFolderPath = Path.Combine(Environment.CurrentDirectory, "temp");
        private bool isCameraRunning = false;
        private bool isRecognizing = false;
        private FilterInfoCollection videoDevices;
        private VideoCaptureDevice videoSource;
        public TrainForm()
        {
            InitializeComponent();
        }
        /////////////////////////////////// Nhóm hàm liên quan đến việc đóng mở form, hiển thị, chỉnh sửa kích thước ảnh, lõi python ///////////////////////////////////


        private void Train_Load(object sender, EventArgs e)
        {

        }

        private void Train_FormClosing(object sender, FormClosingEventArgs e)
        {
            // Dừng camera khi đóng form
            if (videoSource != null && videoSource.IsRunning)
            {
                videoSource.SignalToStop();
                videoSource.WaitForStop();
            }
        }

        private string RunPythonScript(string cmd, string args)
        {
            ProcessStartInfo start = new ProcessStartInfo
            {
                FileName = cmd,
                Arguments = args,
                UseShellExecute = false,
                RedirectStandardOutput = true,
                CreateNoWindow = true // Không hiển thị cửa sổ dòng lệnh
            };

            // Khởi chạy tiến trình
            using (Process process = Process.Start(start))
            {
                // Đọc đầu ra tiêu chuẩn của tiến trình
                using (StreamReader reader = process.StandardOutput)
                {
                    string result = reader.ReadToEnd();
                    // Hiển thị đầu ra trên màn hình console
                    Console.WriteLine(result);
                    return result;
                }
            }
        }

        private void DisplayImageInPictureBox(string file_path, PictureBox PicBox)
        {
            // Đọc ảnh từ tệp
            Image originalImage = Image.FromFile(file_path);

            // Kích thước của picBoxTrain
            int picBoxWidth = PicBox.Width;
            int picBoxHeight = PicBox.Height;

            // Tính toán chiều rộng và chiều cao mới dựa trên kích thước của picBoxTrain
            int newWidth = originalImage.Width;
            int newHeight = originalImage.Height;

            if (newWidth > picBoxWidth)
            {
                newWidth = picBoxWidth;
                newHeight = (int)((double)newWidth / originalImage.Width * originalImage.Height);
            }

            if (newHeight > picBoxHeight)
            {
                newHeight = picBoxHeight;
                newWidth = (int)((double)newHeight / originalImage.Height * originalImage.Width);
            }

            // Tạo ảnh mới với kích thước mới
            Image resizedImage = ResizeImage(originalImage, newWidth, newHeight);

            // Tính toán vị trí để căn giữa ảnh trong picBoxTrain
            int x = (picBoxWidth - newWidth) / 2;
            int y = (picBoxHeight - newHeight) / 2;

            // Tạo một Bitmap mới với kích thước của picBoxTrain
            Bitmap centeredBitmap = new Bitmap(picBoxWidth, picBoxHeight);

            // Tạo một đối tượng Graphics để vẽ ảnh mới vào vị trí giữa
            using (Graphics g = Graphics.FromImage(centeredBitmap))
            {
                g.DrawImage(resizedImage, x, y, newWidth, newHeight);
            }

            // Hiển thị ảnh trong PictureBox
            PicBox.Image = centeredBitmap;
        }

        private Image ResizeImage(Image image, int maxWidth, int maxHeight)
        {
            float aspectRatio = (float)image.Width / image.Height;

            // Tính toán kích thước mới dựa trên tỷ lệ và giới hạn kích thước
            int calculatedWidth = Math.Min(maxWidth, (int)(maxHeight * aspectRatio));
            int calculatedHeight = Math.Min(maxHeight, (int)(maxWidth / aspectRatio));

            // Kiểm tra nếu kích thước mới vượt quá kích thước ban đầu
            if (calculatedWidth > image.Width || calculatedHeight > image.Height)
            {
                calculatedWidth = image.Width;
                calculatedHeight = image.Height;
            }

            // Tạo một Bitmap mới với kích thước mới
            Bitmap resizedBitmap = new Bitmap(calculatedWidth, calculatedHeight);

            // Tạo một đối tượng Graphics để vẽ ảnh mới
            using (Graphics g = Graphics.FromImage(resizedBitmap))
            {
                // Vẽ ảnh mới với kích thước mới và giữ nguyên tỷ lệ
                g.DrawImage(image, 0, 0, calculatedWidth, calculatedHeight);
            }
            return resizedBitmap;
        }
        //////////////////////////////////////////// Nhóm hàm liên quan đến việc huấn luyện ////////////////////////////////////////////
        private bool RunIsSingleFaceFunction(string imagePath)
        {
            string fullPathPythonScript = Path.Combine(currentDirectory, pythonScriptPath).Replace('\\', '/');
            string result = RunPythonScript(pythonExePath, $"{fullPathPythonScript} is_single_face \"{imagePath}\"");
            if (Convert.ToBoolean(result) == false)
            {
                MessageBox.Show($"Vui lòng chọn bức ảnh chỉ có 1 khuôn mặt");
                return Convert.ToBoolean(result);
            }
            else
            {
                // Tiến hành lưu vào Dataset
                string DatasetPath = Path.Combine(currentDirectory, "../../Datasets").Replace('\\', '/');
                string filePath = Path.Combine(DatasetPath, $"{txbName.Text}.png");

                Bitmap originalImage = new Bitmap(ofdTrain.FileName);
                originalImage.Save(filePath, System.Drawing.Imaging.ImageFormat.Png);
                return Convert.ToBoolean(result);
            }
        }
        private void RunEncodeImagesInDataset()
        {
            string fullPathPythonScript = Path.Combine(currentDirectory, pythonScriptPath).Replace('\\', '/');
            string datasetPath = Path.Combine(currentDirectory, "../../Datasets").Replace('\\', '/');
            string encodingFilePath = Path.Combine(currentDirectory, "../../Models/encodings.txt").Replace('\\', '/');
            string trainedPath = $"{datasetPath}/Trained";
            RunPythonScript(pythonExePath, $"\"{fullPathPythonScript}\" encode_images_in_dataset \"{datasetPath}\" \"{encodingFilePath}\" \"{trainedPath}\"");
            MessageBox.Show("Đã huấn luyện xong", "Thông báo", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void btnOpenImageTrain_Click(object sender, EventArgs e)
        {
            // Thiết lập các thuộc tính cho OpenFileDialog
            ofdTrain.Title = "Chọn ảnh đào tạo"; // Tiêu đề của hộp thoại
            ofdTrain.Filter = "Ảnh|*.jpg;*.jpeg;*.png;*.gif";
            ofdTrain.InitialDirectory = Environment.GetFolderPath(Environment.SpecialFolder.MyPictures); // Thư mục mặc định khi mở hộp thoại

            // Hiển thị hộp thoại mở tệp và xác nhận rằng người dùng đã chọn một tệp
            if (ofdTrain.ShowDialog() == DialogResult.OK)
            {
                // Lấy đường dẫn đầy đủ của tệp đã chọn
                selectedFilePathTrain = ofdTrain.FileName;
                try
                {
                    DisplayImageInPictureBox(selectedFilePathTrain, picBoxTrain);
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Không thể mở ảnh: " + ex.Message, "Lỗi", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
        }

        private void btnTrain_Click(object sender, EventArgs e)
        {
            // Kiểm tra xem txbName đã có dữ liệu hay không
            if (string.IsNullOrEmpty(txbName.Text))
            {
                MessageBox.Show("Vui lòng nhập tên trước khi tiếp tục.", "Lỗi", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return; // Ngừng thực hiện khi txbName không có dữ liệu
            }

            // Kiểm tra xem người dùng đã chọn ảnh hay không
            if (selectedFilePathTrain == null)
            {
                MessageBox.Show("Vui lòng chọn ảnh trước khi tiếp tục.", "Lỗi", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return; // Ngừng thực hiện khi người dùng không chọn ảnh
            }
            else
            {
                bool checkSingleFace = RunIsSingleFaceFunction(selectedFilePathTrain);
                if (checkSingleFace)
                {
                    RunEncodeImagesInDataset();
                }
            }
        }
    }
}
