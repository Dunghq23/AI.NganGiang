using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Drawing.Imaging;
using System.Threading;

namespace Recognition
{
    public partial class MainForm : Form
    {


        public MainForm()
        {
            InitializeComponent();
        }
        private void btnTrain_Click(object sender, EventArgs e)
        {
            // Tạm ẩn MainForm
            this.Hide();

            // Tạo và hiển thị TrainForm
            TrainForm trainForm = new TrainForm();
            trainForm.ShowDialog();

            // Hiển thị lại MainForm khi TrainForm đóng
            this.Show();
        }

        private void btnRecognize_Click(object sender, EventArgs e)
        {
            this.Hide();

            RecognizeForm recognizeForm = new RecognizeForm();
            recognizeForm.ShowDialog();

            this.Show();
        }

        private void MainForm_FormClosing(object sender, FormClosingEventArgs e)
        {
            // Kiểm tra xem thư mục temp tồn tại hay không
            if (Directory.Exists(@"./temp"))
            {
                // Nếu tồn tại, thực hiện xóa
                try
                {
                    Directory.Delete(@"./temp", true);
                }
                catch (Exception ex)
                {
                    // Hiển thị thông báo nếu không thể xóa
                    MessageBox.Show("Không thể xóa thư mục temp: " + ex.Message, "Lỗi", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
        }
    }
}
