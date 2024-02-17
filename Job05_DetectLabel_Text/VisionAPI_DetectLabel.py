import os, io
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ServiceAccToken.JSON'

def detect_labels(path):
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    # [START vision_python_migration_label_detection]
    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations
    
    print("Labels:")
    for label in labels:
        print('  - ',label.description)

img_name = 'logos.jpg'
file_path = f'./resources/{img_name}'
detect_labels(file_path)