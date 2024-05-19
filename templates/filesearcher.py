import os

cascade_path = r"C:\Users\Angelo\Downloads\haarcascade_frontalface_default.xml"

if os.path.exists(cascade_path):
    print("File exists and is accessible.")
else:
    print("File does not exist or is not accessible.")
