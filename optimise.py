import os
from PIL import Image


def resize_and_convert_images(source_folder, max_width=800, max_height=450):
    """
    This function resize a given image to 800 X 450
    """
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


def crop_from_l_t_r_b(source_folder, max_width=800, max_height=450):
    """
    This function remove extra pixels from left, top, right and buttom
    """
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

def crop_from_r_b(source_folder, max_width=800, max_height=450):
    """
    This function remove extra pixels from right and buttom
    Starts with 0,0 -> 800, 450
    """
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                file_path = os.path.join(root, file)
                webp_file_path = os.path.splitext(file_path)[0] + '.webp'
                try:
                    with Image.open(file_path) as img:
                        # Calculate cropping area
                        width, height = img.size
                        left = 0
                        top = 0
                        right = left + max_width
                        bottom = top + max_height

                        if right > width:
                            right = width
                            left = width - max_width
                        if bottom > height:
                            bottom = height
                            top = height - max_height

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
    # resize_and_convert_images("netzz/resize")
    # crop_from_l_t_r_b(source_folder)
    crop_from_r_b("netzz/crop_from_r_b")

