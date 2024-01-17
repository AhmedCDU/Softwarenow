'''github repo link https://github.com/AhmedCDU/Softwarenow.git'''

from PIL import Image
import random  # Import the random module for generating numbers

# Open the image
image_path = r"C:\Users\Chicken Milk\Desktop\python\Assignment 2\chapter1.jpg"
image = Image.open(image_path)

# Generate a random number for modifying pixel values
generated_number = random.randint(10, 100)

# Iterate through each pixel and modify it
for y in range(image.height):
    for x in range(image.width):
        # Get the original pixel values
        original_pixel = image.getpixel((x, y))

        # Modify pixel values using the generated number
        modified_pixel = (
            original_pixel[0] + generated_number,
            original_pixel[1] + generated_number,
            original_pixel[2] + generated_number,
        )

        # Set the modified pixel values
        image.putpixel((x, y), modified_pixel)

# Save the new image
output_image_path = r"C:\Users\Chicken Milk\Desktop\python\Assignment 2\chapter1_modified.jpg"
image.save(output_image_path)

# Calculate the sum of red pixel values in the modified image
red_sum_modified = sum(modified_pixel[0] for modified_pixel in image.getdata())
print(f"Sum of red pixel values in the modified image: {red_sum_modified}")
