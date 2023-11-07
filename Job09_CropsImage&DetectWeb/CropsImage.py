import os
from google.cloud import vision
from PIL import Image, ImageDraw


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ServiceAccToken.JSON'
client = vision.ImageAnnotatorClient()


def get_crop_hint(path):
    with open(path, "rb") as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    crop_hints_params = vision.CropHintsParams(aspect_ratios=[16/9])
    image_context = vision.ImageContext(crop_hints_params=crop_hints_params)
    response = client.crop_hints(image=image, image_context=image_context)
    hints = response.crop_hints_annotation.crop_hints
    vertices = hints[0].bounding_poly.vertices
    return vertices

def draw_hint(image_file):
    vects = get_crop_hint(image_file)
    im = Image.open(image_file)
    draw = ImageDraw.Draw(im)
    draw.polygon(
        [
            vects[0].x,
            vects[0].y,
            vects[1].x,
            vects[1].y,
            vects[2].x,
            vects[2].y,
            vects[3].x,
            vects[3].y,
        ],
        None,
        "red",
    )
    im.save("output-hint.jpg", "JPEG")
    print("Saved new image to output-hint.jpg")


def crop_to_hint(image_file):
    vects = get_crop_hint(image_file)

    im = Image.open(image_file)
    im2 = im.crop([vects[0].x, vects[0].y, vects[2].x - 1, vects[2].y - 1])
    im2.save("output-crop.jpg", "JPEG")
    print("Saved new image to output-crop.jpg")

draw_hint("./resources/TokyoTower.jpg")  
crop_to_hint("./resources/TokyoTower.jpg")
