namespace Recognition
{
    partial class TrainForm
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
            this.label1 = new System.Windows.Forms.Label();
            this.txbName = new System.Windows.Forms.TextBox();
            this.btnOpenImageTrain = new System.Windows.Forms.Button();
            this.picBoxTrain = new System.Windows.Forms.PictureBox();
            this.btnTrain = new System.Windows.Forms.Button();
            this.ofdTrain = new System.Windows.Forms.OpenFileDialog();
            ((System.ComponentModel.ISupportInitialize)(this.picBoxTrain)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(23, 15);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(61, 16);
            this.label1.TabIndex = 8;
            this.label1.Text = "Nhập tên";
            // 
            // txbName
            // 
            this.txbName.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.txbName.Location = new System.Drawing.Point(104, 12);
            this.txbName.Name = "txbName";
            this.txbName.Size = new System.Drawing.Size(239, 22);
            this.txbName.TabIndex = 7;
            // 
            // btnOpenImageTrain
            // 
            this.btnOpenImageTrain.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.btnOpenImageTrain.Location = new System.Drawing.Point(22, 478);
            this.btnOpenImageTrain.Name = "btnOpenImageTrain";
            this.btnOpenImageTrain.Size = new System.Drawing.Size(138, 38);
            this.btnOpenImageTrain.TabIndex = 6;
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
            this.picBoxTrain.Location = new System.Drawing.Point(22, 40);
            this.picBoxTrain.Name = "picBoxTrain";
            this.picBoxTrain.Size = new System.Drawing.Size(859, 432);
            this.picBoxTrain.TabIndex = 5;
            this.picBoxTrain.TabStop = false;
            // 
            // btnTrain
            // 
            this.btnTrain.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.btnTrain.Location = new System.Drawing.Point(743, 478);
            this.btnTrain.Name = "btnTrain";
            this.btnTrain.Size = new System.Drawing.Size(138, 38);
            this.btnTrain.TabIndex = 9;
            this.btnTrain.Text = "Huấn luyện";
            this.btnTrain.UseVisualStyleBackColor = true;
            this.btnTrain.Click += new System.EventHandler(this.btnTrain_Click);
            // 
            // ofdTrain
            // 
            this.ofdTrain.FileName = "openFileDialog1";
            // 
            // TrainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(893, 528);
            this.Controls.Add(this.btnTrain);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.txbName);
            this.Controls.Add(this.btnOpenImageTrain);
            this.Controls.Add(this.picBoxTrain);
            this.Name = "TrainForm";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Huấn luyện khuôn mặt";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Train_FormClosing);
            ((System.ComponentModel.ISupportInitialize)(this.picBoxTrain)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox txbName;
        private System.Windows.Forms.Button btnOpenImageTrain;
        private System.Windows.Forms.PictureBox picBoxTrain;
        private System.Windows.Forms.Button btnTrain;
        private System.Windows.Forms.OpenFileDialog ofdTrain;
    }
}