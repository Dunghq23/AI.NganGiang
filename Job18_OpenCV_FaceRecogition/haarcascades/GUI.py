import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import cv2
import os
import subprocess
from PIL import Image, ImageTk

class FaceRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition App")

        self.create_widgets()

    def create_widgets(self):
        # Create tabs
        self.tab_control = ttk.Notebook(self.root)
        self.tab_train = ttk.Frame(self.tab_control)
        self.tab_recognize = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab_train, text='Train')
        self.tab_control.add(self.tab_recognize, text='Recognize')

        self.tab_control.pack(expand=1, fill='both')

        # Train tab
        self.btn_train = ttk.Button(self.tab_train, text="Train", command=self.train_faces)
        self.btn_train.pack(pady=10)

        # Recognize tab
        self.btn_recognize = ttk.Button(self.tab_recognize, text="Recognize", command=self.recognize_faces)
        self.btn_recognize.pack(pady=10)

    def train_faces(self):
        try:
            subprocess.run(['python', 'train.py'], check=True)
            messagebox.showinfo("Training Completed", "Face training completed successfully!")
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Face training failed!")

    def recognize_faces(self):
        try:
            subprocess.run(['python', 'recognition.py'], check=True)
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Face recognition failed!")

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceRecognitionApp(root)
    root.mainloop()
