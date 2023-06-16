# 동영상 파일에서 오디오 파일을 추출하여 다른 경로에 저장

import os
import shutil
from moviepy.editor import *

# 입력 디렉토리의 경로 설정
input_dir = "D:/데이터작업/1.정제/230510/오디오변환이전/230510_001"

# 출력 디렉토리의 경로 설정
output_dir = "D:/데이터작업/1.정제/230510/오디오변환이후/230510_001"

# 아카이브 디렉토리의 경로 설정
archive_dir = "D:/데이터작업/1.정제/230510/오디오변환이후/230510_001"

# 입력 디렉토리의 각 파일을 반복합니다.
for filename in os.listdir(input_dir):
    if filename.endswith(".mp4"):
        # 입력 파일의 경로 설정
        input_file = os.path.join(input_dir, filename)
        
        # 출력 파일의 경로 설정
        output_file = os.path.join(output_dir, os.path.splitext(filename)[0] + ".m4a")
        
        # moviepy를 사용하여 비디오 파일 로드
        video = VideoFileClip(input_file)
        
        # 비디오에서 오디오를 추출하고 m4a로 저장
        audio = video.audio
        audio.write_audiofile(output_file, codec="aac", bitrate="192k")
        
        # 비디오 및 오디오 클립 닫기
        video.close()
        audio.close()
        
        # 입력 파일을 아카이브 디렉토리에 복사
        shutil.copy(input_file, os.path.join(archive_dir, filename))