import os
import cv2
import tkinter as tk
from tkinter import filedialog
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ServiceAccToken.JSON'
client = vision.ImageAnnotatorClient()


def CreateImagePathOrURI(image_path_or_uri):
    image = vision.Image()
    if image_path_or_uri.startswith("http://") or image_path_or_uri.startswith("https://"):
        image.source.image_uri = image_path_or_uri
    else:
        with open(image_path_or_uri, "rb") as image_file:
            content = image_file.read()
        image.content = content
    return image



# ========================================================
def detect_properties(path_or_URI):
    image = CreateImagePathOrURI(path_or_URI)

    response = client.image_properties(image=image)
    props = response.image_properties_annotation

    result = "Properties:\n"
    for color in props.dominant_colors.colors:
        result += f"fraction: {color.pixel_fraction}\n"
        result += f"\tr: {color.color.red}\n"
        result += f"\tg: {color.color.green}\n"
        result += f"\tb: {color.color.blue}\n"
        result += f"\ta: {color.color.alpha}\n"

    return result

def detect_safe_search(path_or_URI):
    image = CreateImagePathOrURI(path_or_URI)

    response = client.safe_search_detection(image=image)
    safe = response.safe_search_annotation

    likelihood_name = (
        "UNKNOWN",
        "VERY_UNLIKELY",
        "UNLIKELY",
        "POSSIBLE",
        "LIKELY",
        "VERY_LIKELY",
    )
    result = "Safe search:"
    result += f"    adult: {likelihood_name[safe.adult]}"
    result += f"    medical: {likelihood_name[safe.medical]}"
    result += f"    spoofed: {likelihood_name[safe.spoof]}"
    result += f"    violence: {likelihood_name[safe.violence]}"
    result += f"    racy: {likelihood_name[safe.racy]}"
    return result

def detect_faces(path_or_URI):
    image = CreateImagePathOrURI(path_or_URI)
    response = client.face_detection(image=image)
    faces= response.face_annotations
    result = f"Found {len(faces)} face."
    image_cv2 = cv2.imread(path_or_URI)
    result = ''
    for face in faces:
        vertices = [(vertex.x, vertex.y) for vertex in face.bounding_poly.vertices]
        x, y, width, height = cv2.boundingRect(np.array(vertices))
        out_vertice = ', '.join(map(str, vertices))
        result += f"\nFace bounds: {out_vertice}"
        # Vẽ hình vuông
        cv2.rectangle(image_cv2, (x, y), (x + width, y + height), (0, 255, 0), 2)
    output_file = "out.jpg"
    cv2.imwrite(output_file, image_cv2)
    result += f"\nWriting to file {output_file}"
    return result

def detect_emotions(path_or_URI):
    image = CreateImagePathOrURI(path_or_URI)
    response = client.face_detection(image=image)
    faceAnnotation = response.face_annotations
    likehood = ('UNKNOWN', 'VERY UNLIKELY', 'UNLIKELY', 'POSSIBLY', 'LIKELY', 'VERY LIKELY')
    result = f"Found {len(faceAnnotation)} face."
    for face in faceAnnotation:
        result += f"\nFaces:"
        result += f'\n    Detection confidence : {round(face.detection_confidence * 100, 2)}'
        result += f'\n    Angry                : {likehood[face.anger_likelihood]}'
        result += f'\n    Joy                  : {likehood[face.joy_likelihood]}'
        result += f'\n    Sorrow               : {likehood[face.sorrow_likelihood]}'
        result += f'\n    Sup                  : {likehood[face.surprise_likelihood]}'
        result += f'\n    Headwear             : {likehood[face.headwear_likelihood]}'
    return result

def detect_labels(path_or_URI):
    image = CreateImagePathOrURI(path_or_URI)
    response = client.label_detection(image=image)
    labels = response.label_annotations
    result = "Labels:"
    for label in labels:
        result += '\n  - ',label.description
    return result
    
def detect_texts(path_or_URI):
    image = CreateImagePathOrURI(path_or_URI)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    result = "Texts:"
    for text in texts:
        result += f'\n"{text.description}"'
        vertices = [
            f"\n({vertex.x},{vertex.y})" for vertex in text.bounding_poly.vertices
        ]
        result += "bounds: {}".format(",".join(vertices))
    return result
    
def detect_landmarks(path_or_URI):
    image = CreateImagePathOrURI(path_or_URI)
    response = client.landmark_detection(image=image)
    landmarks = response.landmark_annotations
    result = "Landmarks:\n"
    for landmark in landmarks:
        result += landmark.description
        for location in landmark.locations:
            lat_lng = location.lat_lng
            result += f"\nLatitude: {lat_lng.latitude}"
            result += f"\nLongitude: {lat_lng.longitude}"
    return result
    
choice_to_function = {
    "Face": detect_faces(),
    "Emotion": detect_emotions(),
    "Label": detect_labels(),
    "Text": detect_texts(),
    "Properties": detect_properties(),
    "Safe": detect_safe_search(),
    "Landmark": detect_landmarks(),
}

app = tk.Tk()
app.title("Image Detection App")

choice_var = tk.StringVar()
choice_label = tk.Label(app, text="Chọn kiểu phát hiện:")
choice_label.pack()
choices = ('Face', 'Emotion', 'Label', 'Text', 'Properties', 'Safe', 'Landmark')
choice_menu = tk.OptionMenu(app, choice_var, *choices)
choice_menu.pack()

img_path_label = tk.Label(app, text="Đường dẫn hình ảnh:")
img_path_label.pack()
img_path_entry = tk.Entry(app)
img_path_entry.pack()
browse_button = tk.Button(app, text="Chọn ảnh", command=browse_image)
browse_button.pack()

detect_button = tk.Button(app, text="Phát hiện", command=detect)
detect_button.pack()

result_text = tk.Text(app)
result_text.pack(fill=tk.BOTH, expand=True)  # Để result_text mở rộng để lấp đầy cửa sổ
result_text.insert(tk.END, "Nội dung cần chèn")

app.mainloop()