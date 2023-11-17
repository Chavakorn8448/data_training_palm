import os

foldername = 'week_6_unripe'

file_list = os.listdir(foldername)

# Define a custom sort key that extracts the numeric portion and converts it to an integer
def sort_key(filename):
    # Split filename and extension
    name, _ = os.path.splitext(filename)
    # Split on underscores and get the last part which should be the number
    number = name.split("_")[-1]
    # Convert the number to an integer and return
    return int(number)

# Sort the file list
sorted_file_list = sorted(file_list, key=sort_key)

# Now, rename files
for i, filename in enumerate(sorted_file_list):
    _, extension = os.path.splitext(filename)  # Split filename and extension
    new_name = str(i + 1) + extension  # Construct new name

    old = os.path.join(foldername, filename)
    new = os.path.join(foldername, new_name)

    os.rename(old, new)

print("Files renamed successfully!")