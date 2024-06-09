import os
from PIL import Image

def resize_and_convert_images(source_folder, max_width=800):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                file_path = os.path.join(root, file)
                webp_file_path = os.path.splitext(file_path)[0] + '.webp'
                try:
                    with Image.open(file_path) as img:
                        # Check if the image width is greater than max_width
                        if img.width > max_width:
                            # Calculate the new height to maintain aspect ratio
                            aspect_ratio = img.height / img.width
                            new_height = int(max_width * aspect_ratio)
                            # Resize the image
                            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
                        
                        # Save the image as WebP
                        img.save(webp_file_path, 'webp', optimize=True, quality=85)
                    print(f'Converted and resized {file_path} to {webp_file_path}')
                except Exception as e:
                    print(f'Failed to convert {file_path}: {e}')

if __name__ == "__main__":
    source_folder = "netzz/09-where-iphone-backup-is-stored-in-windows-10/"
    resize_and_convert_images(source_folder)
