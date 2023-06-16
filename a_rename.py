# 파일명 일괄 변경 프로그램

import os

def batch_rename_files(directory, old_string, new_string):
    for filename in os.listdir(directory):
        if old_string in filename:
            # Construct the new file name
            new_filename = filename.replace(old_string, new_string)
            # Get the full paths of the old and new files
            old_filepath = os.path.join(directory, filename)
            new_filepath = os.path.join(directory, new_filename)
            # Rename the file
            os.rename(old_filepath, new_filepath)
            print(f"Renamed '{filename}' to '{new_filename}'")

def change_string_in_batch(directory, old_string, new_string):
    for filename in os.listdir(directory):
        if old_string in filename:
            # Construct the new file name
            new_filename = filename.replace(old_string, new_string)
            # Get the full paths of the old and new files
            old_filepath = os.path.join(directory, filename)
            new_filepath = os.path.join(directory, new_filename)
            # Rename the file
            os.rename(old_filepath, new_filepath)
            print(f"Renamed '{filename}' to '{new_filename}'")

# 파일 경로, 원래 문자열, 바꿀 문자열을 입력하세요.
directory = 'D:/데이터작업/1.편성표분할작업/11/05'
old_string = '1105' 
new_string = '1104'  

# Call the function to rename the files
batch_rename_files(directory, old_string, new_string)