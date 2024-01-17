using System;
using System.Drawing;
using System.IO;
using System.Threading.Tasks;
using System.Windows.Forms;

using AxWMPLib;
using Emgu.CV;
using Emgu.CV.CvEnum;
using Emgu.CV.Structure;

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

                MessageBox.Show("Hình ảnh đã được trích xuất và lưu lại.", "Thông báo", MessageBoxButtons.OK, MessageBoxIcon.Information);

                // Đặt capturing về false sau khi quá trình trích xuất hoàn tất
                capturing = false;
            }
            else
            {
                MessageBox.Show("Vui lòng chọn một tệp video.", "Thông báo", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }

        private void ExtractImages()
        {
            while (capture != null && capture.Ptr != IntPtr.Zero && capture.Read(frame))
            {
                ProcessFrameAndSave(frame);
                frameIndex++;
            }

            // Đã đọc hết video, dừng quá trình trích xuất
            capture.Stop();
            capture.Dispose();
        }

        private void ProcessFrameAndSave(Mat frame)
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


            // Lấy đường dẫn thư mục hiện tại của ứng dụng
            string currentDirectory = AppDomain.CurrentDomain.BaseDirectory;

            // Kết hợp đường dẫn tương đối với thư mục hiện tại để có đường dẫn đầy đủ
            string relativePath = @"..\..\..\ExtractImages"; // Đường dẫn tương đối từ thư mục hiện tại
            string extractPath = Path.Combine(currentDirectory, relativePath);

            // Đảm bảo rằng thư mục đích tồn tại và tạo nó nếu chưa có
            if (!Directory.Exists(extractPath))
            {
                Directory.CreateDirectory(extractPath);
            }

            // Lưu frame thành ảnh
            string videoFilePath = WinMediaPlayer.URL;
            string videoFileName = Path.GetFileNameWithoutExtension(videoFilePath);

            string fileName = $"{videoFileName}_frame_{frameIndex + 1}.png";
            string filePath = Path.Combine(extractPath, fileName);

            img.Save(filePath);

        }
    }
}
