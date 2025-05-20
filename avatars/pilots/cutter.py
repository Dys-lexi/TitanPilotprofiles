from PIL import Image
import os

# Supported image extensions
IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')

def crop_images_to_square_from_left():
    for filename in os.listdir('.'):
        if filename.lower().endswith(IMAGE_EXTENSIONS):
            try:
                with Image.open(filename) as img:
                    width, height = img.size
                    crop_size = height  # Target size is the image height

                    if width < crop_size:
                        print(f"Skipping {filename}: width < height")
                        continue

                    # Vertically center the crop area
                    top = 0
                    left = 0
                    right = left + crop_size
                    bottom = top + crop_size

                    cropped_img = img.crop((left, top, right, bottom))

                    # Save the cropped image
                    name, ext = os.path.splitext(filename)
                    new_filename = f"{name}_cropped{ext}"
                    cropped_img.save(new_filename)
                    print(f"Saved cropped image: {new_filename}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

if __name__ == '__main__':
    crop_images_to_square_from_left()
