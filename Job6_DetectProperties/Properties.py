import os, io
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ServiceAccToken.JSON'

def detect_properties(image_path_or_uri):
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    if image_path_or_uri.startswith("http://") or image_path_or_uri.startswith("https://"):
        image = vision.Image()
        image.source.image_uri = image_path_or_uri
    else:
        with open(image_path_or_uri, "rb") as image_file:
            content = image_file.read()
        image = vision.Image(content=content)

    response = client.image_properties(image=image)
    props = response.image_properties_annotation
    print("Properties:")

    for color in props.dominant_colors.colors:
        print(f"fraction: {color.pixel_fraction}")
        print(f"\tr: {color.color.red}")
        print(f"\tg: {color.color.green}")
        print(f"\tb: {color.color.blue}")
        print(f"\ta: {color.color.alpha}")

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )

# Sử dụng hàm detect_properties với đối số là đường dẫn cục bộ hoặc URL
detect_properties("https://nv.edu.vn/wp-content/uploads/2021/01/Nhat-Ban-dat-nuoc-mat-troi-moc-1.jpg")


# img_path = f'./resources/recycle.jpg'
# detect_properties(img_path)
detect_properties("https://nv.edu.vn/wp-content/uploads/2021/01/Nhat-Ban-dat-nuoc-mat-troi-moc-1.jpg")

print("Ha Quang Dung")