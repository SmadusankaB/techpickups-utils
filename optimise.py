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

def resize_and_convert_images(source_folder, max_width=800, max_height=450):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                file_path = os.path.join(root, file)
                webp_file_path = os.path.splitext(file_path)[0] + '.webp'
                try:
                    with Image.open(file_path) as img:
                        # Calculate the aspect ratio
                        aspect_ratio = img.width / img.height
                        
                        # Determine new dimensions based on max width and max height
                        if img.width > max_width or img.height > max_height:
                            if aspect_ratio > 1:  # Landscape orientation
                                new_width = min(max_width, img.width)
                                new_height = int(new_width / aspect_ratio)
                            else:  # Portrait orientation
                                new_height = min(max_height, img.height)
                                new_width = int(new_height * aspect_ratio)
                            
                            # Resize the image
                            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                        
                        # Save the image as WebP
                        img.save(webp_file_path, 'webp', optimize=True, quality=85)
                    print(f'Converted and resized {file_path} to {webp_file_path}')
                except Exception as e:
                    print(f'Failed to convert {file_path}: {e}')

if __name__ == "__main__":
    source_folder = "netzz/graphics"
    # crop_and_convert_images(source_folder)
    resize_and_convert_images(source_folder)
