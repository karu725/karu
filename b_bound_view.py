import os
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw

def draw_bounding_boxes(directory, box_width=1):
    files = os.listdir(directory)
    for file in files:
        if file.endswith('.xml'):
            xml_path = os.path.join(directory, file)
            tree = ET.parse(xml_path)
            root = tree.getroot()

            image_name = root.find('filename').text
            image_path = os.path.join(directory, image_name)
            image = Image.open(image_path)

            draw = ImageDraw.Draw(image)

            for obj in root.findall('object'):
                bbox = obj.find('bndbox')
                xmin = int(bbox.find('xmin').text)
                ymin = int(bbox.find('ymin').text)
                xmax = int(bbox.find('xmax').text)
                ymax = int(bbox.find('ymax').text)

                draw.rectangle([(xmin, ymin), (xmax, ymax)], outline='red', width=box_width)

            output_path = os.path.join(directory, image_name)
            image.save(output_path)

# 작업 대상 경로 입력
directory = 'D:/data/2_bound/face/15_face'
draw_bounding_boxes(directory, box_width=2)
