import os
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ServiceAccToken.JSON'
client = vision.ImageAnnotatorClient()

def detect_safe_search(image_path_or_uri):
    if image_path_or_uri.startswith("http://") or image_path_or_uri.startswith("https://"):
        image = vision.Image()
        image.source.image_uri = image_path_or_uri
    else:
        with open(image_path_or_uri, "rb") as image_file:
            content = image_file.read()
        image = vision.Image(content=content)

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
detect_safe_search("./resources/threatening.jpg")