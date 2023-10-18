import os, io
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ServiceAccToken.JSON'

def detect_safe_search(image_path_or_uri):
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

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

    print(f"adult: {likelihood_name[safe.adult]}")
    print(f"medical: {likelihood_name[safe.medical]}")
    print(f"spoofed: {likelihood_name[safe.spoof]}")
    print(f"violence: {likelihood_name[safe.violence]}")
    print(f"racy: {likelihood_name[safe.racy]}")

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )

# Sử dụng hàm detect_safe_search với đối số là đường dẫn cục bộ hoặc URL
# detect_safe_search("https://nv.edu.vn/wp-content/uploads/2021/01/Nhat-Ban-dat-nuoc-mat-troi-moc-1.jpg")
detect_safe_search("./resources/threatening.jpg")