# img2ascii

`img2ascii` is a Python script that converts images into ASCII art. The script reads an input image, converts it to grayscale, and maps the brightness of each pixel to a corresponding ASCII character.

## Features

- Convert any image to ASCII art.
- Adjustable output dimensions for the ASCII art.
- Optional saving of the ASCII art to a text file.
- View the ASCII art directly using OpenCV.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy
- Pillow (`PIL`)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/img2ascii.git
    cd img2ascii
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:
    ```sh
    python img2ascii.py
    ```

2. Provide the path to the image file when prompted:
    ```sh
    Path: path/to/your/image.jpg
    ```

3. Specify the height of the ASCII art:
    ```sh
    Height: 50
    ```

4. Choose whether to save the ASCII art to a text file:
    ```sh
    Save? (y/n): y
    ```

5. If you chose to save, the ASCII art will be saved to `Output.txt` in your Downloads folder.

## Example

```sh
$ python img2ascii.py
Path: example.jpg
Height: 50
Save? (y/n): y
Saved as "Output.txt"
```

## Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.
