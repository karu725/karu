import cv2
import os
import xml.etree.ElementTree as ET

# 전역 변수
start_point = None
end_point = None
bounding_boxes = []
temp_box = None
current_image_index = 0
image_paths = []

# 마우스 콜백 기능
def draw_bounding_box(event, x, y, flags, param):
    global start_point, end_point, bounding_boxes, temp_box

    if event == cv2.EVENT_LBUTTONDOWN:
        start_point = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        end_point = (x, y)
        bounding_boxes.append((start_point, end_point))
        cv2.rectangle(image, start_point, end_point, (0, 255, 0), 2)
        temp_box = None
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        temp_box = (start_point, (x, y))

    # 임시 상자로 이미지 업데이트
    temp_image = image.copy()
    if temp_box is not None:
        cv2.rectangle(temp_image, temp_box[0], temp_box[1], (0, 255, 0), 2)
    cv2.imshow('Image', temp_image)

# 바운딩박스를 XML 형식으로 저장하는 기능
def save_bounding_boxes_to_xml(file_path, bounding_boxes):
    root = ET.Element("annotations")

    for i, (start, end) in enumerate(bounding_boxes):
        box_element = ET.SubElement(root, "box")
        ET.SubElement(box_element, "label").text = f"Box {i+1}"
        ET.SubElement(box_element, "xmin").text = str(start[0])
        ET.SubElement(box_element, "ymin").text = str(start[1])
        ET.SubElement(box_element, "xmax").text = str(end[0])
        ET.SubElement(box_element, "ymax").text = str(end[1])

    tree = ET.ElementTree(root)
    tree.write(file_path)

# 다음 순서 이미지 처리 기능
def process_next_image():
    global current_image_index, image_paths, image

    if current_image_index < len(image_paths):
        image_path = image_paths[current_image_index]
        image = cv2.imread(image_path)
        cv2.imshow('Image', image)
        cv2.setWindowTitle('Image', f'Image - {image_path}')
        current_image_index += 1
    else:
        print("더 이상 처리할 이미지가 없습니다.")
        cv2.destroyAllWindows()

# 검수 대상 이미지 파일 경로 설정
images_directory = 'D:/data/1pairing/11/face/01_face/5_face'

# 디렉터리 내부의 모든 이미지 검색
image_extensions = ['.jpg', '.jpeg', '.png']
for root, dirs, files in os.walk(images_directory):
    for file in files:
        ext = os.path.splitext(file)[1]
        if ext.lower() in image_extensions:
            image_paths.append(os.path.join(root, file))

# 윈도우 생성 및 콜백 함수 설정
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', draw_bounding_box)

# 첫 번째 이미지 처리
process_next_image()

while True:
    key = cv2.waitKey(0) & 0xFF

    # 바운딩박스를 리셋하시려면 'w'를 누르십시오.
    if key == ord('w'):
        bounding_boxes = []
        image = cv2.imread(image_paths[current_image_index - 1])
        cv2.imshow('Image', image)

    # 다음 이미지로 넘기려면 'e'를 누르십시오. (적합)
    elif key == ord('e'):
        if bounding_boxes:
            image_path = image_paths[current_image_index - 1]
            xml_file_path = os.path.splitext(image_path)[0] + '.xml'
            save_bounding_boxes_to_xml(xml_file_path, bounding_boxes)
            bounding_boxes = []
            process_next_image()
        else:
            print("바운딩박스가 레이블되지 않았습니다.")

    # xml 생성을 스킵하려면 'q'를 누르십시오. (부적합)
    elif key == ord('q'):
        current_image_index += 1
        if current_image_index <= len(image_paths):
            image = cv2.imread(image_paths[current_image_index - 1])
            cv2.imshow('Image', image)
        else:
            print("No more images to display.")


    # 프로그램을 종료하려면 'z'을 누르십시오.
    elif key == ord('z'):
        break

cv2.destroyAllWindows()
