import re
import requests
import cairosvg
from io import BytesIO
from PIL import Image
import os
import sys

def process_svg_to_png(link):
    try:
        # Fetch the page content
        response = requests.get(link)
        response.raise_for_status()
        content = response.text

        # Find the SVG URL
        match = re.search(r'https://mansoorbarri\.com/og/og-image-[a-zA-Z0-9]+\.svg', content)
        if not match:
            print("No matching SVG link found.")
            return

        svg_url = match.group(0)
        print(f"Found SVG URL: {svg_url}")

        # Fetch the SVG content
        svg_response = requests.get(svg_url)
        svg_response.raise_for_status()

        # Convert SVG to PNG
        png_data = cairosvg.svg2png(bytestring=svg_response.content)

        # Save the PNG to the Downloads folder
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        output_path = os.path.join(downloads_path, "svg.png")

        with open(output_path, "wb") as png_file:
            png_file.write(png_data)

        print(f"PNG image saved successfully at {output_path}!")
    except requests.RequestException as e:
        print(f"An error occurred while fetching the URL: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py {URL}")
        sys.exit(1)

    link = sys.argv[1]
    process_svg_to_png(link)
