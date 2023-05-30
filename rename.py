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

# Provide the directory, old string, and new string
directory = 'D:/데이터작업/1.편성표분할작업/11/05'  # Replace with the actual directory path
old_string = '1105'  # Replace with the old string you want to replace
new_string = '1104'  # Replace with the new string

# Call the function to rename the files
batch_rename_files(directory, old_string, new_string)