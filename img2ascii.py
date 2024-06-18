import cv2
import numpy as np
from PIL import ImageFont, Image, ImageDraw
import os
from typing import Optional, Tuple

# Define brightness to symbol mapping
BRIGHTNESS_SYMBOLS = ["$", "X", "x", "+", "=", ":", ".", " "]

# Convert pixel brightness to symbol
def num2sym(brightness: float) -> str:
    index = min(int(brightness * len(BRIGHTNESS_SYMBOLS)), len(BRIGHTNESS_SYMBOLS) - 1)
    return BRIGHTNESS_SYMBOLS[index]

# Get brightness of a pixel
def get_bright(x: int, y: int, img: np.ndarray) -> float:
    pixel_color = img[x, y]
    return round(pixel_color / 255, 2)

# Create PIL canvas
def create_PIL(x: int, y: int, f: Optional[np.ndarray] = None) -> Tuple[ImageDraw.Draw, Image.Image]:
    if f is None:
        image = np.full((x, y, 3), 255, dtype=np.uint8)  # Fill with 255 for a white image
    else:
        image = cv2.cvtColor(f, cv2.COLOR_BGR2RGB)
    image_pil = Image.fromarray(image)
    draw = ImageDraw.Draw(image_pil)
    return draw, image_pil

# Draw text on image with white text and black background
def add_text(text: str, pos: Tuple[int, int], x: int, y: int, rows: int, f: Optional[np.ndarray] = None) -> np.ndarray:
    try:
        font_path = r"C:\Users\user\Desktop\AI\img2sym\consolas.ttf"

        if not os.path.exists(font_path):
            raise FileNotFoundError
        font = ImageFont.truetype(font_path, int(x / rows))
    except (FileNotFoundError, OSError):
        font = ImageFont.load_default()
        print("Warning: Using default font. Ensure 'consolas.ttf' is in the same directory as the script.")
    
    draw, image_pil = create_PIL(x, y, f)
    # Draw white text on a black background
    draw.rectangle([(pos[0], pos[1]), (pos[0] + len(text) * int(x / rows), pos[1] + int(x / rows))], fill="black")
    draw.text(pos, text, font=font, fill="white")
    image_with_text = np.array(image_pil)
    return image_with_text

# Main function to convert image to ASCII art
def img2ascii(img_path: str) -> Optional[np.ndarray]:
    try:
        img = cv2.imread(img_path)
        if img is None:
            raise ValueError("Image not found")

        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        nh, nw = img_gray.shape

        awd = int(input('Height: '))
        n = nh // awd
        height, width = nh // n, nw // n
        img_resized = cv2.resize(img_gray, (width, height))

        ascii_img = np.zeros((height, width), dtype=str)

        for i in range(height):
            for j in range(width):
                brightness = get_bright(i, j, img_resized)
                ascii_img[i, j] = num2sym(1 - brightness)

        hh = nh / height

        if nh > nw:
            img_height = nw * 2
            img_width = nw
        else:
            img_height = nh
            img_width = nh * 2

        output_string = ''
        img_with_text = add_text(''.join(ascii_img[0]), (0, 0), img_height, img_width, height)
        output_string += ' '.join(ascii_img[0]) + '\n'

        for i in range(1, height):
            img_with_text = add_text(''.join(ascii_img[i]), (0, i * hh), img_height, img_width, height, img_with_text)
            output_string += ' '.join(ascii_img[i]) + '\n'

        save = input('Save? (y/n): ')
        if save.lower() == 'y':
            with open(r"C:\Users\user\Downloads\Output.txt", "w") as text_file:
                text_file.write(output_string)
                print('Saved as "Output.txt"')

        h, w, c = img_with_text.shape
        img_with_text = img_with_text[0:h, 0:h + int(n * 3.33)]
        img_with_text = cv2.resize(img_with_text, (nw // 2, nh // 2))

        return img_with_text

    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    img_path = input('Path: ')
    result_img = img2ascii(img_path)
    if result_img is not None:
        cv2.imshow("ASCII Art", result_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
