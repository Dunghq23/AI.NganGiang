using AxWMPLib;
using Emgu.CV;
using Emgu.CV.CvEnum;
using Emgu.CV.Structure;
using System;
using System.Drawing;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Job20_OpenVideos_ExtractImages_UsingEmguCV
{
    public partial class FormMain : Form
    {
        private VideoCapture capture;
        private int frameIndex = 0;
        private bool capturing = false;
        private Mat frame = new Mat(); // Khai báo ở đây để tránh tạo đối tượng mới mỗi lần Capture_ImageGrabbed được gọi

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
                // Tính toán chiều rộng và chiều cao mới của frame dựa trên tỷ lệ khung hình
                double aspectRatio = (double)frame.Width / frame.Height;
                int newWidth = picBox.Width;
                int newHeight = (int)(newWidth / aspectRatio);

                // Resize frame theo chiều rộng và chiều cao của picBox
                CvInvoke.Resize(frame, frame, new Size(newWidth, newHeight));

                Image<Bgr, byte> img = frame.ToImage<Bgr, byte>();
                Bitmap bitmap = img.ToBitmap();

                // Hiển thị frame trên PictureBox
                picBox.Invoke((MethodInvoker)delegate
                {
                    picBox.Image = bitmap;
                    picBox.Invalidate();
                });

                // Tăng chỉ số frame
                frameIndex++;
            }

            // Đã đọc hết video, dừng quá trình trích xuất
            capture.Stop();
            capture.Dispose();
        }
    }
}
