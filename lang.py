import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def get_filenames(path):
    filenames = []
    for root, dirs, files in os.walk(path):
        for file in files:
            filenames.append(file)
    return filenames

def extract_file_parts(filenames):
    extracted_parts = []
    for filename in filenames:
        part1 = filename[22:27]  # Extracts lang[5:10]
        part2 = filename[28:33]  # Extracts lang[10:15]
        extracted_parts.append((part1, part2))
    return extracted_parts

# Example usage
directory_path = "D:/데이터작업/1.편성표분할작업/11/04"  # Replace with the desired directory path
filenames = get_filenames(directory_path)
extracted_parts = extract_file_parts(filenames)

# Print the extracted parts
for part1, part2 in extracted_parts:
    print(part1, part2)

