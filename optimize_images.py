import re
import os

def optimize_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match base64 image strings
    # We'll replace them with placeholder paths for now to reduce size
    # In a real scenario, we'd extract them to files.
    
    # 1. Replace HOD photo
    hod_pattern = r'src="data:image/jpeg;base64,[^"]+"'
    content = re.sub(hod_pattern, 'src="images/OgundareBS.JPG"', content, count=1)

    # 2. Replace staff photos in the staffData object
    # The pattern matches "photo: " followed by the base64 string
    staff_photo_pattern = r'photo:\s*"data:image/[^;]+;base64,[^"]+"'
    
    def staff_replacer(match):
        # We could potentially extract the name here if we wanted to be fancy
        # but for speed, let's just use a generic placeholder or a name-based one if possible
        return 'photo: "images/logo.png"' # Using logo as a temporary placeholder that exists

    content = re.sub(staff_photo_pattern, staff_replacer, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    optimize_html('index.html')
    print("Optimization complete.")
