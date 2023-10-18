import os
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

# Sử dụng hàm detect_safe_search với đối số là đường dẫn cục bộ hoặc URL
detect_safe_search("https://images2.thanhnien.vn/Uploaded/ngocthanh/2022_08_06/dieu-tri-sot-xuat-huyet-cho-tre-em-tai-benh-vien-benh-nhiet-doi-tp-5822.jpg")
# detect_safe_search("./resources/threatening.jpg")

# img_path = f'./resources/recycle.jpg'
# detect_properties(img_path)
# detect_properties("https://nv.edu.vn/wp-content/uploads/2021/01/Nhat-Ban-dat-nuoc-mat-troi-moc-1.jpg")