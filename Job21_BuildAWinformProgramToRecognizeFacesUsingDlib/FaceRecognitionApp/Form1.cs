using System;
using System.Collections.Generic;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Windows.Forms;
using Emgu.CV;
using Emgu.CV.CvEnum;
using Emgu.CV.Dnn;
using Emgu.CV.Face;
using Emgu.CV.Structure;
using Emgu.CV.Util;


namespace FaceRecognitionApp
{
    public partial class Form1 : Form
    {
        private VideoCapture _capture = new VideoCapture();
        private CascadeClassifier _faceCascade;
        private EigenFaceRecognizer recognizer;

        public Form1()
        {
            InitializeComponent();
            _faceCascade = new CascadeClassifier(@"..\..\Models\haarcascade_frontalface_default.xml");
        }

        
        private void Form1_Load(object sender, EventArgs e)
        {
            if (_capture != null && _capture.IsOpened)
            {
                int pictureBoxWidth = pictureBox.Width;
                int pictureBoxHeight = pictureBox.Height;

                _capture.Set(CapProp.FrameWidth, pictureBoxWidth);
                _capture.Set(CapProp.FrameHeight, pictureBoxHeight);

                Application.Idle += ProcessFrame;

                recognizer = new EigenFaceRecognizer();
                recognizer.Read(@"..\..\Models\trained_model.yml"); // Đọc mô hình đã huấn luyện
            }
            else
            {
                MessageBox.Show("Không thể mở Camera!");
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

        // Khi thực hiện nhận diện khuôn mặt
        private void ProcessFrame(object sender, EventArgs e)
        {
            Mat frame = _capture.QueryFrame();

            if (frame != null)
            {
                Mat grayFrame = new Mat();
                CvInvoke.CvtColor(frame, grayFrame, ColorConversion.Bgr2Gray);

                Rectangle[] faces = _faceCascade.DetectMultiScale(
                    grayFrame,
                    scaleFactor: 1.1,
                    minNeighbors: 5,
                    minSize: Size.Empty
                );

                // Load ánh xạ nhãn và tên người từ tệp văn bản
                Dictionary<int, string> labelMapping = LoadLabelMapping();

                foreach (Rectangle face in faces)
                {

                    Mat faceRegion = new Mat(grayFrame, face);

                    // Thêm dòng lệnh này để resize ảnh thử nghiệm cùng kích thước với ảnh đào tạo
                    CvInvoke.Resize(faceRegion, faceRegion, new Size(100, 100));

                    var prediction = recognizer.Predict(faceRegion); // Kết quả dự đoán
                    int predictedLabel = prediction.Label; // Lấy nhãn từ kết quả dự đoán

                    if (labelMapping.ContainsKey(predictedLabel))
                    {
                        string recognizedPerson = labelMapping[predictedLabel]; // Tên người dự đoán
                        string labelDisplay = $"{recognizedPerson}";

                        // Hiển thị thông tin trên frame
                        CvInvoke.Rectangle(frame, face, new MCvScalar(0, 255, 0), 2);
                        CvInvoke.PutText(frame, labelDisplay, new Point(face.X, face.Bottom + 20), FontFace.HersheyComplex, 0.5, new MCvScalar(255, 255, 255), 1);
                    }
                    else
                    {
                        // Trường hợp không có ánh xạ cho nhãn
                        string labelDisplay = $"Unknown";
                        CvInvoke.Rectangle(frame, face, new MCvScalar(0, 0, 255), 2);
                        CvInvoke.PutText(frame, labelDisplay, new Point(face.X, face.Bottom + 20), FontFace.HersheyComplex, 0.5, new MCvScalar(0, 0, 255), 1);
                    }
                }

                CvInvoke.Flip(frame, frame, FlipType.Horizontal);
                pictureBox.Image = frame.ToImage<Bgr, byte>().ToBitmap();
            }
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (_capture != null && _capture.IsOpened)
            {
                _capture.Dispose();
            }
        }

        private const int NumImagesToCapture = 50;

        private void btnTrain_Click(object sender, EventArgs e)
        {
            string result = RunPythonScript("python", $"../../Python/train.py --dataset ../../dataset --model ../../Models/trained_model.yml --mapping ../../Models/label_mapping.txt");
            MessageBox.Show("Đã huấn luyện thành công", "Thông báo", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }
       

        private void btnGetFace_Click(object sender, EventArgs e)
        {
            string personName = txbName.Text.Trim();

            if (!string.IsNullOrEmpty(personName))
            {
                string userFolderPath = Path.Combine(@"..\..\Dataset\", personName);
                Directory.CreateDirectory(userFolderPath);

                for (int i = 0; i < NumImagesToCapture; i++)
                {
                    Mat frame = _capture.QueryFrame();
                    if (frame != null)
                    {
                        Mat grayFrame = new Mat();
                        CvInvoke.CvtColor(frame, grayFrame, ColorConversion.Bgr2Gray);

                        Rectangle[] faces = _faceCascade.DetectMultiScale(
                            grayFrame,
                            scaleFactor: 1.1,
                            minNeighbors: 5,
                            minSize: Size.Empty
                        );

                        if (faces.Length > 0)
                        {
                            Rectangle face = faces[0];
                            Mat faceRegion = new Mat(grayFrame, face);
                            string imagePath = Path.Combine(userFolderPath, $"{personName}_{i}.jpg");
                            CvInvoke.Imwrite(imagePath, faceRegion.ToImage<Gray, byte>());
                            CvInvoke.Rectangle(frame, face, new MCvScalar(0, 255, 0), 2);
                        }

                        CvInvoke.Flip(frame, frame, FlipType.Horizontal);
                        pictureBox.Image = frame.ToImage<Bgr, byte>().ToBitmap();
                    }
                }

                MessageBox.Show("Đã chụp và lưu ảnh khuôn mặt cho " + personName);
                
                txbName.Text = null;
            }
            else
            {
                MessageBox.Show("Tên người dùng không hợp lệ.");
            }
        }


        private Dictionary<int, string> LoadLabelMapping()
        {
            string mappingFilePath = @"..\..\Models\label_mapping.txt";
            Dictionary<int, string> labelMapping = new Dictionary<int, string>();

            if (File.Exists(mappingFilePath))
            {
                foreach (string line in File.ReadLines(mappingFilePath))
                {
                    string[] parts = line.Split(' ');
                    if (parts.Length == 2 && int.TryParse(parts[0], out int label))
                    {
                        string personName = parts[1];
                        labelMapping[label] = personName;
                    }
                }
            }

            return labelMapping;
        }
        
    }
}
