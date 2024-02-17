namespace Recognition
{
    partial class RecognizeForm
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
            this.txbRecognize = new System.Windows.Forms.TextBox();
            this.btnCamera = new System.Windows.Forms.Button();
            this.btnRecognize = new System.Windows.Forms.Button();
            this.btnOpenImageRecognize = new System.Windows.Forms.Button();
            this.picBoxRecognize = new System.Windows.Forms.PictureBox();
            this.ofdRecognize = new System.Windows.Forms.OpenFileDialog();
            ((System.ComponentModel.ISupportInitialize)(this.picBoxRecognize)).BeginInit();
            this.SuspendLayout();
            // 
            // txbRecognize
            // 
            this.txbRecognize.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.txbRecognize.Font = new System.Drawing.Font("Microsoft Sans Serif", 7.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.txbRecognize.ForeColor = System.Drawing.Color.Red;
            this.txbRecognize.Location = new System.Drawing.Point(557, 565);
            this.txbRecognize.Name = "txbRecognize";
            this.txbRecognize.ReadOnly = true;
            this.txbRecognize.Size = new System.Drawing.Size(239, 22);
            this.txbRecognize.TabIndex = 14;
            // 
            // btnCamera
            // 
            this.btnCamera.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.btnCamera.Location = new System.Drawing.Point(333, 494);
            this.btnCamera.Name = "btnCamera";
            this.btnCamera.Size = new System.Drawing.Size(138, 38);
            this.btnCamera.TabIndex = 17;
            this.btnCamera.Text = "Mở Camera";
            this.btnCamera.UseVisualStyleBackColor = true;
            this.btnCamera.Click += new System.EventHandler(this.btnCamera_Click);
            // 
            // btnRecognize
            // 
            this.btnRecognize.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.btnRecognize.Location = new System.Drawing.Point(658, 494);
            this.btnRecognize.Name = "btnRecognize";
            this.btnRecognize.Size = new System.Drawing.Size(138, 38);
            this.btnRecognize.TabIndex = 16;
            this.btnRecognize.Text = "Nhận dạng";
            this.btnRecognize.UseVisualStyleBackColor = true;
            this.btnRecognize.Click += new System.EventHandler(this.btnRecognize_Click);
            // 
            // btnOpenImageRecognize
            // 
            this.btnOpenImageRecognize.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.btnOpenImageRecognize.Location = new System.Drawing.Point(496, 494);
            this.btnOpenImageRecognize.Name = "btnOpenImageRecognize";
            this.btnOpenImageRecognize.Size = new System.Drawing.Size(138, 38);
            this.btnOpenImageRecognize.TabIndex = 15;
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
            this.picBoxRecognize.Location = new System.Drawing.Point(5, 30);
            this.picBoxRecognize.Name = "picBoxRecognize";
            this.picBoxRecognize.Size = new System.Drawing.Size(797, 439);
            this.picBoxRecognize.TabIndex = 13;
            this.picBoxRecognize.TabStop = false;
            // 
            // ofdRecognize
            // 
            this.ofdRecognize.FileName = "openFileDialog_Recognize";
            // 
            // RecognizeForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(814, 616);
            this.Controls.Add(this.txbRecognize);
            this.Controls.Add(this.btnCamera);
            this.Controls.Add(this.btnRecognize);
            this.Controls.Add(this.btnOpenImageRecognize);
            this.Controls.Add(this.picBoxRecognize);
            this.Name = "RecognizeForm";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "RecognizeForm";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.RecognizeForm_FormClosing);
            this.Load += new System.EventHandler(this.RecognizeForm_Load);
            ((System.ComponentModel.ISupportInitialize)(this.picBoxRecognize)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox txbRecognize;
        private System.Windows.Forms.Button btnCamera;
        private System.Windows.Forms.Button btnRecognize;
        private System.Windows.Forms.Button btnOpenImageRecognize;
        private System.Windows.Forms.PictureBox picBoxRecognize;
        private System.Windows.Forms.OpenFileDialog ofdRecognize;
    }
}