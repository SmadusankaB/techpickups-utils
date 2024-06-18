import os
from PIL import Image


def fill_and_resize_images_with_background(source_folder, max_width=800, max_height=450, background_color=(240, 240, 240)):
    """
    This function resizes and pads an image to fit within 800 x 450 pixels, maintaining aspect ratio.
    It adds padding with the specified background color to meet the max dimensions if needed.
    """
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                file_path = os.path.join(root, file)
                webp_file_path = os.path.splitext(file_path)[0] + '.webp'
                try:
                    with Image.open(file_path) as img:
                        # Ensure the image has an alpha channel if needed
                        img = img.convert('RGBA')

                        # Calculate the aspect ratio
                        aspect_ratio = img.width / img.height

                        # Resize image based on aspect ratio
                        if aspect_ratio > 1:
                            new_width = min(max_width, img.width)
                            new_height = int(new_width / aspect_ratio)
                        else:
                            new_height = min(max_height, img.height)
                            new_width = int(new_height * aspect_ratio)

                        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

                        # Create new image with max dimensions and specified background color
                        new_img = Image.new('RGB', (max_width, max_height), background_color)

                        # Calculate paste position to center the image
                        paste_x = (max_width - new_width) // 2
                        paste_y = (max_height - new_height) // 2

                        # Paste the resized image onto the background image
                        new_img.paste(img.convert('RGB'), (paste_x, paste_y))

                        # Save the image as WebP
                        new_img.save(webp_file_path, 'webp', optimize=True, quality=85)

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
    fill_and_resize_images_with_background("netzz/resize")
    # crop_from_l_t_r_b(source_folder)
    # crop_from_r_b("netzz/crop_from_r_b")

