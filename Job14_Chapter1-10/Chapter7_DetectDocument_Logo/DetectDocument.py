import os
from enum import Enum
from google.cloud import vision
from PIL import Image, ImageDraw

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ServiceAccToken.JSON'
client = vision.ImageAnnotatorClient()

class FeatureType(Enum):
    PAGE = 1
    BLOCK = 2
    PARA = 3
    WORD = 4
    SYMBOL = 5

def draw_boxes(image, bounds, color):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        draw.polygon(
            [
                bound.vertices[0].x, bound.vertices[0].y,
                bound.vertices[1].x, bound.vertices[1].y,
                bound.vertices[2].x, bound.vertices[2].y,
                bound.vertices[3].x, bound.vertices[3].y,
            ],
            None,
            color,
        )
    return image

def get_document_bounds(image_file, feature):
    bounds = []
    with open(image_file, "rb") as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.document_text_detection(image=image)
    document = response.full_text_annotation
    
    for page in document.pages:
        for block in page.blocks:
            print(f'\nBlock confidence: {format(block.confidence)}')
            for paragraph in block.paragraphs:
                print(f'\nParagraph confidence: {format(paragraph.confidence)}')
                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    print(f'\n      Word text: {word_text} (confidence: {format(word.confidence)})')
                    for symbol in word.symbols:
                        print(f'\n            Symbol: {symbol.text} (confidence: {format(symbol.confidence)})')
                        if feature == FeatureType.SYMBOL:
                            bounds.append(symbol.bounding_box)
                    if feature == FeatureType.WORD:
                        bounds.append(word.bounding_box)
                if feature == FeatureType.PARA:
                    bounds.append(paragraph.bounding_box)
            if feature == FeatureType.BLOCK:
                bounds.append(block.bounding_box)
        if feature == FeatureType.PAGE:
            bounds.append(page.bounding_box)
    return bounds

def render_doc_text(filein, fileout):
    image = Image.open(filein)
    bounds = get_document_bounds(filein, FeatureType.BLOCK)
    draw_boxes(image, bounds, "blue")
    if fileout != 0:
        image.save(fileout)
    else:
        image.show()

img_path = './resources/HQD.jpg'
# render_doc_text(img_path, 'output_image.jpg') 
render_doc_text(img_path, 0) 
