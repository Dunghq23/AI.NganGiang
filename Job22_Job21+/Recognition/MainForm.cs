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
    }
}