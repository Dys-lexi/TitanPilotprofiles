from PIL import Image
import os

# Supported image extensions
IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')

def crop_images_to_square_top_centered(width_percent=40):
    if not (0 < width_percent <= 100):
        raise ValueError("width_percent must be between 0 and 100")

    for filename in os.listdir('.'):
        if filename.lower().endswith(IMAGE_EXTENSIONS):
            try:
                with Image.open(filename) as img:
                    original_width, original_height = img.size

                    # Calculate the new width based on the percentage
                    new_width = int((width_percent / 100.0) * original_width)
                    if new_width > original_height:
                        print(f"Skipping {filename}: resulting square would exceed image height")
                        continue

                    # Center horizontally
                    left = (original_width - new_width) // 2
                    right = left + new_width

                    # Align to the top
                    top = 0
                    bottom = top + new_width  # height = width to make it square

                    if bottom > original_height:
                        print(f"Skipping {filename}: height too small for desired crop")
                        continue

                    cropped_img = img.crop((left, top, right, bottom))

                    # Save the cropped image
                    name, ext = os.path.splitext(filename)
                    new_filename = f"{name}_cropped{ext}"
                    cropped_img.save(new_filename)
                    print(f"Saved cropped image: {new_filename}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

if __name__ == '__main__':
    crop_images_to_square_top_centered(width_percent=80)  # Set your desired width %
