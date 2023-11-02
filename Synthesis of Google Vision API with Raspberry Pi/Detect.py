import os, sys
import cv2
import numpy as np
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



# ========================================================
def detect_properties(path_or_URI):
    image = CreateImagePathOrURI(path_or_URI)

    response = client.image_properties(image=image)
    props = response.image_properties_annotation
    
    print("Properties:")
    for color in props.dominant_colors.colors:
        print(f"fraction: {color.pixel_fraction}")
        print(f"\tr: {color.color.red}")
        print(f"\tg: {color.color.green}")
        print(f"\tb: {color.color.blue}")
        print(f"\ta: {color.color.alpha}")

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
    print("Safe search:")
    print(f"    adult: {likelihood_name[safe.adult]}")
    print(f"    medical: {likelihood_name[safe.medical]}")
    print(f"    spoofed: {likelihood_name[safe.spoof]}")
    print(f"    violence: {likelihood_name[safe.violence]}")
    print(f"    racy: {likelihood_name[safe.racy]}")

def detect_faces(path_or_URI):
    image = CreateImagePathOrURI(path_or_URI)
    response = client.face_detection(image=image)
    faces= response.face_annotations
    print(f"Found {len(faces)} face.")
    image_cv2 = cv2.imread(path_or_URI)
    for face in faces:
        vertices = [(vertex.x, vertex.y) for vertex in face.bounding_poly.vertices]
        x, y, width, height = cv2.boundingRect(np.array(vertices))
        out_vertice = ', '.join(map(str, vertices))
        print(f"Face bounds: {out_vertice}")
        # Vẽ hình vuông
        cv2.rectangle(image_cv2, (x, y), (x + width, y + height), (0, 255, 0), 2)
    output_file = "out.jpg"
    cv2.imwrite(output_file, image_cv2)
    print(f"Writing to file {output_file}")

def detect_emotions(path_or_URI):
    image = CreateImagePathOrURI(path_or_URI)
    response = client.face_detection(image=image)
    faceAnnotation = response.face_annotations
    likehood = ('UNKNOWN', 'VERY UNLIKELY', 'UNLIKELY', 'POSSIBLY', 'LIKELY', 'VERY LIKELY')
    print(f"Found {len(faceAnnotation)} face.")
    for face in faceAnnotation:
        print(f"Faces:")
        print(f'    Detection confidence : {round(face.detection_confidence * 100, 2)}')
        print(f'    Angry                : {likehood[face.anger_likelihood]}')
        print(f'    Joy                  : {likehood[face.joy_likelihood]}')
        print(f'    Sorrow               : {likehood[face.sorrow_likelihood]}')
        print(f'    Sup                  : {likehood[face.surprise_likelihood]}')
        print(f'    Headwear             : {likehood[face.headwear_likelihood]}')
        print()

def detect_labels(path_or_URI):
    image = CreateImagePathOrURI(path_or_URI)
    response = client.label_detection(image=image)
    labels = response.label_annotations
    print("Labels:")
    for label in labels:
        print('  - ',label.description)

def detect_texts(path_or_URI):
    image = CreateImagePathOrURI(path_or_URI)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    print("Texts:")
    for text in texts:
        print(f'\n"{text.description}"')
        vertices = [
            f"({vertex.x},{vertex.y})" for vertex in text.bounding_poly.vertices
        ]
        print("bounds: {}".format(",".join(vertices)))

def detect_landmarks(path_or_URI):
    image = CreateImagePathOrURI(path_or_URI)
    response = client.landmark_detection(image=image)
    landmarks = response.landmark_annotations
    print("Landmarks:")
    for landmark in landmarks:
        print(landmark.description)
        for location in landmark.locations:
            lat_lng = location.lat_lng
            print(f"Latitude: {lat_lng.latitude}")
            print(f"Longitude: {lat_lng.longitude}")
# ======================= Main ==========================
if len(sys.argv) != 3:
    print("Sử dụng: python Detect.py [Properties|Safe] [img_path]")
else:
    choise = ('Face', 'Emotion', 'Label', 'Text', 'Properties', 'Safe', 'Landmark')
    option = sys.argv[1]
    img_path = sys.argv[2]
    if option == "Face":
        detect_faces(img_path)
    elif option == "Emotion":
        detect_emotions(img_path)
    elif option == "Label":
        detect_labels(img_path)
    elif option == "Text":
        detect_texts(img_path)
    elif option == "Properties":
        detect_properties(img_path)
    elif option == "Safe":
        detect_safe_search(img_path)
    elif option == "Landmark":
        detect_landmarks(img_path)
    else:
        print("Không rõ lựa chọn:", option)
