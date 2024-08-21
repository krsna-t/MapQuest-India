from PIL import Image

# Open the original image
original_image_path = "india.gif"
resized_image_path = "map_resized.gif"

with Image.open(original_image_path) as img:
    # Resize the image (change the size as needed)
    new_size = (700,560)  # Width and Height
    resized_img = img.resize(new_size)
    resized_img.save(resized_image_path)
