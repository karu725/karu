from moviepy.editor import *

# 입력 디렉토리의 경로 설정
input_dir = "D:/데이터작업/1.정제/230510/오디오변환이전"
# 출력 디렉토리의 경로 설정
output_dir = "D:/데이터작업/1.정제/230510/오디오변환이후"

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
        
        # Close the video and audio clips
        video.close()
        audio.close()