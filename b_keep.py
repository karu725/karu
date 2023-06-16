# jpg 파일 중 동일한 파일명의 xml 파일이 없을 경우 jpg 경로 이동

import os
import shutil

source_dir = "D:/data/2_bound/face/15_face"  # 작업 대상 경로 입력
target_dir = "D:/data/2_bound/face/15_face/keep"  # 보류 파일 이동 경로 입력

for file_name in os.listdir(source_dir):
    if file_name.lower().endswith(".jpg"):
        jpg_file = os.path.join(source_dir, file_name)
        xml_file = os.path.join(source_dir, os.path.splitext(file_name)[0] + ".xml")
        
        if not os.path.exists(xml_file):
            target_file = os.path.join(target_dir, file_name)
            shutil.move(jpg_file, target_file)
            print(f"Moved {file_name} to {target_dir}.")
