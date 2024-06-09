import os
from PIL import Image

def convert_images_to_webp(source_folder):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                file_path = os.path.join(root, file)
                webp_file_path = os.path.splitext(file_path)[0] + '.webp'
                try:
                    with Image.open(file_path) as img:
                        img.save(webp_file_path, 'webp', optimize=True, quality=60)
                    print(f'Converted {file_path} to {webp_file_path}')
                except Exception as e:
                    print(f'Failed to convert {file_path}: {e}')

if __name__ == "__main__":
    source_folder = "netzz/"
    convert_images_to_webp(source_folder)
