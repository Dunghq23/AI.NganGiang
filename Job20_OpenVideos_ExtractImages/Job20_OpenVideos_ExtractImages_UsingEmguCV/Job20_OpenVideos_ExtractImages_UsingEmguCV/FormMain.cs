using AxWMPLib;
using Emgu.CV;
using Emgu.CV.CvEnum;
using Emgu.CV.Structure;
using System;
using System.Drawing;
using System.IO;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Job20_OpenVideos_ExtractImages_UsingEmguCV
{
    public partial class FormMain : Form
    {
        private VideoCapture capture;
        private int frameIndex = 0;
        private bool capturing = false;
        private Mat frame = new Mat();

        public FormMain()
        {
            InitializeComponent();
        }

        private void btnOpenVideo_Click(object sender, EventArgs e)
        {
            OpenFileDialog ofd = new OpenFileDialog();
            ofd.Title = "Chọn video";
            ofd.Filter = "Tất cả các file|*.*|Video Files|*.avi;*.mp4;*.wmv|Tệp AVI|*.avi|Tệp MP4|*.mp4|Tệp WMV|*.wmv";

            if (ofd.ShowDialog() == DialogResult.OK)
            {
                string selectedFilePath = ofd.FileName;
                WinMediaPlayer.URL = selectedFilePath;
                WinMediaPlayer.Ctlcontrols.play();

                // Khởi tạo VideoCapture từ đường dẫn video
                capture = new VideoCapture(selectedFilePath);
            }
        }

        private async void btnExtractImage_Click(object sender, EventArgs e)
        {
            if (capture != null && !capturing)
            {
                capturing = true;

                // Tạo một Task chạy quá trình trích xuất ảnh từ video
                await Task.Run(() => ExtractImages());

                MessageBox.Show("Hình ảnh đã được trích xuất và hiển thị trên PictureBox.", "Thông báo", MessageBoxButtons.OK, MessageBoxIcon.Information);

                // Đặt capturing về false sau khi quá trình trích xuất hoàn tất
                capturing = false;
            }
            else
            {
                MessageBox.Show("Quá trình trích xuất đang diễn ra hoặc bạn chưa chọn một tệp video.", "Thông báo", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }

        private void ExtractImages()
        {
            while (capture != null && capture.Ptr != IntPtr.Zero && capture.Read(frame))
            {
                ProcessAndDisplayFrame(frame);
                frameIndex++;
            }

            // Đã đọc hết video, dừng quá trình trích xuất
            capture.Stop();
            capture.Dispose();
        }

        private void ProcessAndDisplayFrame(Mat frame)
        {
            // Tính toán chiều rộng và chiều cao mới của frame dựa trên tỷ lệ khung hình
            double aspectRatio = (double)frame.Width / frame.Height;

            // Lấy kích thước hiện tại của PictureBox
            int picBoxWidth = picBox.Width;
            int picBoxHeight = picBox.Height;

            // Tính toán chiều rộng và chiều cao mới của frame dựa trên tỷ lệ khung hình và kích thước của PictureBox
            int newWidth = picBoxWidth;
            int newHeight = (int)(newWidth / aspectRatio);

            // Nếu chiều cao mới vượt quá chiều cao của PictureBox, thì tính lại kích thước dựa trên chiều cao
            if (newHeight > picBoxHeight)
            {
                newHeight = picBoxHeight;
                newWidth = (int)(newHeight * aspectRatio);
            }

            // Resize frame theo chiều rộng và chiều cao mới
            CvInvoke.Resize(frame, frame, new Size(newWidth, newHeight));

            Image<Bgr, byte> img = frame.ToImage<Bgr, byte>();
            Bitmap bitmap = img.ToBitmap();

            // Hiển thị frame trên PictureBox
            picBox.Invoke((MethodInvoker)delegate
            {
                picBox.Image = bitmap;
                picBox.Invalidate();
            });
        }

        private void btnSaveImages_Click(object sender, EventArgs e)
        {
            if (!string.IsNullOrEmpty(WinMediaPlayer.URL))
            {
                string videoFilePath = WinMediaPlayer.URL;

                // Lấy tên của tệp video mà không bao gồm phần mở rộng
                string videoFileName = Path.GetFileNameWithoutExtension(videoFilePath);

                using (var capture = new VideoCapture(videoFilePath))
                {
                    Mat frame = new Mat();
                    int i = 0;

                    // Hiển thị hộp thoại để chọn thư mục lưu
                    using (FolderBrowserDialog folderBrowserDialog = new FolderBrowserDialog())
                    {
                        folderBrowserDialog.Description = "Chọn thư mục để lưu ảnh";

                        if (folderBrowserDialog.ShowDialog() == DialogResult.OK)
                        {
                            string extractPath = folderBrowserDialog.SelectedPath;

                            while (capture.Read(frame)) // Đọc từng frame từ video
                            {
                                ProcessFrameAndSave(frame, extractPath, videoFileName, ref i);
                            }

                            MessageBox.Show($"Hình ảnh đã được trích xuất và lưu vào thư mục: {extractPath}", "Thông báo", MessageBoxButtons.OK, MessageBoxIcon.Information);
                        }
                    }
                }
            }
            else
            {
                MessageBox.Show("Vui lòng chọn một tệp video.", "Thông báo", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }

        private void ProcessFrameAndSave(Mat frame, string extractPath, string videoFileName, ref int i)
        {
            ProcessAndDisplayFrame(frame);

            // Chuyển đổi frame thành hình ảnh Bitmap
            Image<Bgr, byte> img = frame.ToImage<Bgr, byte>();
            Bitmap bitmap = img.ToBitmap();

            // Đặt tên file dựa trên tên của video và chỉ số frame
            string fileName = $"{videoFileName}_frame_{i + 1}.png";

            // Đường dẫn đầy đủ của file
            string filePath = Path.Combine(extractPath, fileName);

            // Lưu frame thành ảnh
            img.Save(filePath);

            i++;
        }
    }
}