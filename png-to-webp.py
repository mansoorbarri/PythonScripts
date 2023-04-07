# Import the Image module from the Python Imaging Library (PIL) 
from PIL import Image
# Import the os module to work with files and directories
import os 

# Define a function named "convert_png_to_webp"
def convert_png_to_webp():
    # Prompt the user to enter the path to the input PNG file and store it in a variable named "input_path"
    input_path = input("Enter the path to the input PNG file: ")
    # Prompt the user to enter the path where the output WebP file should be saved and store it in a variable named "output_path"
    output_path = input("Enter the path where the output WebP file should be saved: ")
    
    # Use the "os.path.abspath" method to get the absolute path of the input and output paths
    input_abs_path = os.path.abspath(os.path.join('/home/anar/', input_path))
    output_abs_path = os.path.abspath(os.path.join('/home/anar/', output_path))

    # Use the "with" statement to open the input PNG file using the Image module from PIL 
    # and store it in a variable named "img"
    with Image.open(input_path) as img:
        # Use the "save" method to save the opened image as a WebP file 
        # and store it in the output path specified by the user 
        img.save(output_path, 'webp')

# Call the "convert_png_to_webp" function to execute the code 
convert_png_to_webp()
