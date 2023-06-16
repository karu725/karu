# jpg 파일 중 동일한 파일명의 xml 파일이 없을 경우 jpg 일괄 삭제

import os

source_dir = "D:/data/2_bound/face/01_face"  # 작업 대상 경로 입력

for file_name in os.listdir(source_dir):
    if file_name.lower().endswith(".jpg"):
        jpg_file = os.path.join(source_dir, file_name)
        xml_file = os.path.join(source_dir, os.path.splitext(file_name)[0] + ".xml")
        
        if not os.path.exists(xml_file):
            os.remove(jpg_file)
            print(f"Deleted {file_name}.")
