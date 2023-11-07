import os

# Replace the folder_path with the path to your folder containing the files
folder_path = "the_palm_killer-2/valid/labels"

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        # Split the filename into two parts: the part before ".jpg" and the extension
        parts = filename.rsplit('.txt', 1)

        # Replace all periods with underscores in the part before ".jpg"
        new_filename = parts[0].replace('.', '_') + '.txt'

        # Combine the modified part and the extension to get the new filename
        if len(parts) == 2:
            new_filename = os.path.join(folder_path, new_filename)

            # Rename the file
            os.rename(os.path.join(folder_path, filename), new_filename)

print("Renaming complete.")
