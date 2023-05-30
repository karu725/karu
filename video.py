from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os

# 시작 시간과 끝 시간의 초 단위를 수동으로 기입하면 비디오 파일이 분할되어 파일로 저장됩니다.

def cut_video(input_file, output_file, start_time, end_time):
    base_path = os.path.dirname(output_file)
    file_name = os.path.splitext(os.path.basename(output_file))[0]
    file_ext = os.path.splitext(os.path.basename(output_file))[1]
    
    start_time_str = str(start_time).zfill(2) if start_time > 0 else '0'
    end_time_str = str(end_time).zfill(2)
    
    output_file_with_times = f"{file_name}_{start_time_str}_{end_time_str}{file_ext}"
    output_path = os.path.join(base_path, output_file_with_times)
    
    ffmpeg_extract_subclip(input_file, start_time, end_time, targetname=output_path)
    print(f"Video cut and saved as '{output_file_with_times}'")

input_file = "D:/데이터작업/0.병합작업/11/E20201105_00001.mp4"      
output_file = "D:/데이터작업/1.편성표분할작업/11/05/E20201105_00001.mp4"    
start_time = 26820                      
end_time = 27000                   

cut_video(input_file, output_file, start_time, end_time)