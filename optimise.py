import os
from PIL import Image

def crop_and_convert_images(source_folder, max_width=800, max_height=450):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                file_path = os.path.join(root, file)
                webp_file_path = os.path.splitext(file_path)[0] + '.webp'
                try:
                    with Image.open(file_path) as img:
                        # Calculate cropping area
                        width, height = img.size
                        left = (width - max_width) / 2
                        top = (height - max_height) / 2
                        right = (width + max_width) / 2
                        bottom = (height + max_height) / 2

                        # Ensure we do not go out of bounds
                        left = max(0, left)
                        top = max(0, top)
                        right = min(width, right)
                        bottom = min(height, bottom)

                        # Crop the center of the image
                        img = img.crop((left, top, right, bottom))

                        # Resize the image if necessary to ensure it matches max dimensions
                        img = img.resize((max_width, max_height), Image.Resampling.LANCZOS)

                        # Save the image as WebP
                        img.save(webp_file_path, 'webp', optimize=True, quality=85)
                    print(f'Converted and cropped {file_path} to {webp_file_path}')
                except Exception as e:
                    print(f'Failed to convert {file_path}: {e}')

if __name__ == "__main__":
    source_folder = "netzz/"
    crop_and_convert_images(source_folder)
