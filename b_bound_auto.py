import cv2
import numpy as np
import xml.etree.ElementTree as ET
import os

model_file = 'res10_300x300_ssd_iter_140000_fp16.caffemodel'
config_file = 'deploy.prototxt.txt'

net = cv2.dnn.readNetFromCaffe(config_file, model_file)

image_dir = 'D:/data/2_bound/face/test'
image_paths = [os.path.join(image_dir, file) for file in os.listdir(image_dir) if file.endswith('.jpg')]

for image_path in image_paths:
    image = cv2.imread(image_path)
    (h, w) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0), swapRB=True, crop=False)
    net.setInput(blob)
    detections = net.forward()

    annotation = ET.Element("annotation")
    filename = ET.SubElement(annotation, "filename")
    filename.text = image_path.split('/')[-1]

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.3:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (x, y, x2, y2) = box.astype("int")

            cv2.rectangle(image, (x, y), (x2, y2), (0, 255, 0), 2)
            text = f'({x}, {y})'
            cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            object_info = ET.SubElement(annotation, "object")
            object_name = ET.SubElement(object_info, "name")
            object_name.text = "face"

            bndbox = ET.SubElement(object_info, "bndbox")
            xmin = ET.SubElement(bndbox, "xmin")
            xmin.text = str(x)
            ymin = ET.SubElement(bndbox, "ymin")
            ymin.text = str(y)
            xmax = ET.SubElement(bndbox, "xmax")
            xmax.text = str(x2)
            ymax = ET.SubElement(bndbox, "ymax")
            ymax.text = str(y2)

            width = ET.SubElement(bndbox, "width")
            width.text = str(x2 - x)
            height = ET.SubElement(bndbox, "height")
            height.text = str(y2 - y)

    cv2.imshow("Face Detection", image)
    key = cv2.waitKey(0)

    if key == ord('w') or key == ord('W'):
        continue  # Skip saving XML file

    tree = ET.ElementTree(annotation)
    xml_file_path = image_path.replace('.jpg', '.xml')
    tree.write(xml_file_path)

cv2.destroyAllWindows()


