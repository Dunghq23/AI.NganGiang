from google.cloud import vision
import os
import cv2
import numpy as np

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ServiceAccToken.JSON'
client = vision.ImageAnnotatorClient()
