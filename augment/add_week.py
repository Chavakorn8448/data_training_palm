import os

# Directory path
dir_path = 'week_9_almost_clean'

# Iterate over each file in the directory
for filename in os.listdir(dir_path):
    # Get the absolute path of the file
    filepath = os.path.join(dir_path, filename)

    # Check if it's a file and not a directory
    if os.path.isfile(filepath):
        # Split the file name and its extension
        base, ext = os.path.splitext(filename)
        
        # Construct the new name
        new_name = base + '_9' + ext
        
        # Get the new absolute path
        new_filepath = os.path.join(dir_path, new_name)
        
        # Rename the file
        os.rename(filepath, new_filepath)

print("Renaming complete!")