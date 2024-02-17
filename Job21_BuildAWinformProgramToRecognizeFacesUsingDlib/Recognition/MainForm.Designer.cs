namespace Recognition
{
    partial class MainForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.splitContainer1 = new System.Windows.Forms.SplitContainer();
            this.btnTrain = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.txbName = new System.Windows.Forms.TextBox();
            this.btnOpenImageTrain = new System.Windows.Forms.Button();
            this.picBoxTrain = new System.Windows.Forms.PictureBox();
            this.txbRecognize = new System.Windows.Forms.TextBox();
            this.btnCamera = new System.Windows.Forms.Button();
            this.btnRecognize = new System.Windows.Forms.Button();
            this.btnOpenImageRecognize = new System.Windows.Forms.Button();
            this.picBoxRecognize = new System.Windows.Forms.PictureBox();
            this.ofdTrain = new System.Windows.Forms.OpenFileDialog();
            this.ofdRecognize = new System.Windows.Forms.OpenFileDialog();
            this.label2 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).BeginInit();
            this.splitContainer1.Panel1.SuspendLayout();
            this.splitContainer1.Panel2.SuspendLayout();
            this.splitContainer1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picBoxTrain)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picBoxRecognize)).BeginInit();
            this.SuspendLayout();
            // 
            // splitContainer1
            // 
            this.splitContainer1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.splitContainer1.Location = new System.Drawing.Point(0, 0);
            this.splitContainer1.Name = "splitContainer1";
            // 
            // splitContainer1.Panel1
            // 
            this.splitContainer1.Panel1.Controls.Add(this.label2);
            this.splitContainer1.Panel1.Controls.Add(this.btnTrain);
            this.splitContainer1.Panel1.Controls.Add(this.label1);
            this.splitContainer1.Panel1.Controls.Add(this.txbName);
            this.splitContainer1.Panel1.Controls.Add(this.btnOpenImageTrain);
            this.splitContainer1.Panel1.Controls.Add(this.picBoxTrain);
            // 
            // splitContainer1.Panel2
            // 
            this.splitContainer1.Panel2.Controls.Add(this.txbRecognize);
            this.splitContainer1.Panel2.Controls.Add(this.btnCamera);
            this.splitContainer1.Panel2.Controls.Add(this.btnRecognize);
            this.splitContainer1.Panel2.Controls.Add(this.btnOpenImageRecognize);
            this.splitContainer1.Panel2.Controls.Add(this.picBoxRecognize);
            this.splitContainer1.Size = new System.Drawing.Size(1148, 589);
            this.splitContainer1.SplitterDistance = 583;
            this.splitContainer1.TabIndex = 0;
            // 
            // btnTrain
            // 
            this.btnTrain.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.btnTrain.Location = new System.Drawing.Point(426, 472);
            this.btnTrain.Name = "btnTrain";
            this.btnTrain.Size = new System.Drawing.Size(138, 38);
            this.btnTrain.TabIndex = 4;
            this.btnTrain.Text = "Huấn luyện";
            this.btnTrain.UseVisualStyleBackColor = true;
            this.btnTrain.Click += new System.EventHandler(this.btnTrain_Click);
            // 
            // label1
            // 
            this.label1.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(244, 437);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(61, 16);
            this.label1.TabIndex = 3;
            this.label1.Text = "Nhập tên";
            // 
            // txbName
            // 
            this.txbName.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.txbName.Location = new System.Drawing.Point(325, 434);
            this.txbName.Name = "txbName";
            this.txbName.Size = new System.Drawing.Size(239, 22);
            this.txbName.TabIndex = 2;
            // 
            // btnOpenImageTrain
            // 
            this.btnOpenImageTrain.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.btnOpenImageTrain.Location = new System.Drawing.Point(23, 425);
            this.btnOpenImageTrain.Name = "btnOpenImageTrain";
            this.btnOpenImageTrain.Size = new System.Drawing.Size(138, 38);
            this.btnOpenImageTrain.TabIndex = 1;
            this.btnOpenImageTrain.Text = "Chọn ảnh";
            this.btnOpenImageTrain.UseVisualStyleBackColor = true;
            this.btnOpenImageTrain.Click += new System.EventHandler(this.btnOpenImageTrain_Click);
            // 
            // picBoxTrain
            // 
            this.picBoxTrain.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.picBoxTrain.BackColor = System.Drawing.Color.Transparent;
            this.picBoxTrain.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picBoxTrain.Location = new System.Drawing.Point(23, 14);
            this.picBoxTrain.Name = "picBoxTrain";
            this.picBoxTrain.Size = new System.Drawing.Size(541, 405);
            this.picBoxTrain.TabIndex = 0;
            this.picBoxTrain.TabStop = false;
            // 
            // txbRecognize
            // 
            this.txbRecognize.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.txbRecognize.Font = new System.Drawing.Font("Microsoft Sans Serif", 7.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.txbRecognize.ForeColor = System.Drawing.Color.Red;
            this.txbRecognize.Location = new System.Drawing.Point(269, 539);
            this.txbRecognize.Name = "txbRecognize";
            this.txbRecognize.ReadOnly = true;
            this.txbRecognize.Size = new System.Drawing.Size(239, 22);
            this.txbRecognize.TabIndex = 5;
            // 
            // btnCamera
            // 
            this.btnCamera.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.btnCamera.Location = new System.Drawing.Point(45, 468);
            this.btnCamera.Name = "btnCamera";
            this.btnCamera.Size = new System.Drawing.Size(138, 38);
            this.btnCamera.TabIndex = 7;
            this.btnCamera.Text = "Mở Camera";
            this.btnCamera.UseVisualStyleBackColor = true;
            this.btnCamera.Click += new System.EventHandler(this.btnOpenCamera_Click);
            // 
            // btnRecognize
            // 
            this.btnRecognize.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.btnRecognize.Location = new System.Drawing.Point(370, 468);
            this.btnRecognize.Name = "btnRecognize";
            this.btnRecognize.Size = new System.Drawing.Size(138, 38);
            this.btnRecognize.TabIndex = 6;
            this.btnRecognize.Text = "Nhận dạng";
            this.btnRecognize.UseVisualStyleBackColor = true;
            this.btnRecognize.Click += new System.EventHandler(this.btnRecognize_Click);
            // 
            // btnOpenImageRecognize
            // 
            this.btnOpenImageRecognize.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.btnOpenImageRecognize.Location = new System.Drawing.Point(208, 468);
            this.btnOpenImageRecognize.Name = "btnOpenImageRecognize";
            this.btnOpenImageRecognize.Size = new System.Drawing.Size(138, 38);
            this.btnOpenImageRecognize.TabIndex = 5;
            this.btnOpenImageRecognize.Text = "Chọn ảnh";
            this.btnOpenImageRecognize.UseVisualStyleBackColor = true;
            this.btnOpenImageRecognize.Click += new System.EventHandler(this.btnOpenImageRecognize_Click);
            // 
            // picBoxRecognize
            // 
            this.picBoxRecognize.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.picBoxRecognize.BackColor = System.Drawing.Color.Transparent;
            this.picBoxRecognize.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picBoxRecognize.Location = new System.Drawing.Point(21, 12);
            this.picBoxRecognize.Name = "picBoxRecognize";
            this.picBoxRecognize.Size = new System.Drawing.Size(517, 405);
            this.picBoxRecognize.TabIndex = 1;
            this.picBoxRecognize.TabStop = false;
            // 
            // ofdTrain
            // 
            this.ofdTrain.FileName = "openFileDialog_Train";
            // 
            // ofdRecognize
            // 
            this.ofdRecognize.FileName = "openFileDialog_Recognize";
            // 
            // label2
            // 
            this.label2.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 8F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.ForeColor = System.Drawing.Color.CornflowerBlue;
            this.label2.Location = new System.Drawing.Point(3, 563);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(572, 17);
            this.label2.TabIndex = 5;
            this.label2.Text = "Lưu ý: Bạn nên huấn luyện mỗi người nhiều ảnh từ nhiều góc độ để cải thiện độ chí" +
    "nh xác";
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1148, 589);
            this.Controls.Add(this.splitContainer1);
            this.Name = "MainForm";
            this.Text = "Nhận diện khuôn mặt";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.MainForm_FormClosing);
            this.Load += new System.EventHandler(this.MainForm_Load);
            this.splitContainer1.Panel1.ResumeLayout(false);
            this.splitContainer1.Panel1.PerformLayout();
            this.splitContainer1.Panel2.ResumeLayout(false);
            this.splitContainer1.Panel2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).EndInit();
            this.splitContainer1.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.picBoxTrain)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picBoxRecognize)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.SplitContainer splitContainer1;
        private System.Windows.Forms.PictureBox picBoxTrain;
        private System.Windows.Forms.PictureBox picBoxRecognize;
        private System.Windows.Forms.Button btnRecognize;
        private System.Windows.Forms.Button btnOpenImageRecognize;
        private System.Windows.Forms.OpenFileDialog ofdTrain;
        private System.Windows.Forms.OpenFileDialog ofdRecognize;
        private System.Windows.Forms.Button btnTrain;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox txbName;
        private System.Windows.Forms.Button btnOpenImageTrain;
        private System.Windows.Forms.Button btnCamera;
        private System.Windows.Forms.TextBox txbRecognize;
        private System.Windows.Forms.Label label2;
    }
}

