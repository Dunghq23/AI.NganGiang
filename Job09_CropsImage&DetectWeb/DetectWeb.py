import os
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ServiceAccToken.JSON'
client = vision.ImageAnnotatorClient()

def annotate(path):
    if path.startswith("http") or path.startswith("gs:"):
        image = vision.Image()
        image.source.image_uri = path
    else:
        with open(path, "rb") as image_file:
            content = image_file.read()
        image = vision.Image(content=content)
    web_detection = client.web_detection(image=image).web_detection
    return web_detection

# ['best_guess_labels'          : Nội dung chung của hình ảnh
# , 'full_matching_images'      : Trùng khớp hoàn toàn với bức ảnh đầu vào
# , 'pages_with_matching_images': Các trang web chứa hình ảnh giống hoặc liên quan với hình ảnh đầu vào
# , 'partial_matching_images'   : Các hình ảnh trên trang web trùng khớp 1 phần với hình ảnh đầu vào
# , 'visually_similar_images'   : Tương tự như về mặt hình ảnh với hình ảnh đầu vào
# , 'web_entities'              : Các đối tượng hoặc thực thể liên quan được tìm thấy trên web]

def report(annotations):
    if annotations.pages_with_matching_images:
        print(
            f"\n{len(annotations.pages_with_matching_images)} Pages with matching images retrieved"
        )
        for page in annotations.pages_with_matching_images:
            print(f"Url   : {page.url}")
    if annotations.full_matching_images:
        print(f"\n{len(annotations.full_matching_images)} Full Matches found: ")
        for image in annotations.full_matching_images:
            print(f"Url  : {image.url}")
    if annotations.partial_matching_images:
        print(f"\n{len(annotations.partial_matching_images)} Partial Matches found: ")
        for image in annotations.partial_matching_images:
            print(f"Url  : {image.url}")
    if annotations.web_entities:
        print(f"\n{len(annotations.web_entities)} Web entities found: ")
        for entity in annotations.web_entities:
            print(f"Score      : {entity.score}")
            print(f"Description: {entity.description}")
            
report(annotate("./resources/keangnam.jpg"))
# report(annotate("https://dynamic-media-cdn.tripadvisor.com/media/photo-o/18/d1/66/35/getlstd-property-photo.jpg?w=1200&h=1200&s=1"))  

