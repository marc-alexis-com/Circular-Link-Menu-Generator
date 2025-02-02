# Circular Link Menu Generator

I wanted to do the same as this 2000s McDonald circle nav :

![2024-10-13 09 09 40](https://github.com/user-attachments/assets/785c2101-17cb-483b-9e39-6420f4b56869)

Basically a round image and a bunch of links evenly spaced around it.

This Python script generates a CSS file that positions menu links around a central circular image for use in a webpage. It takes into account link sizes, ensures proper spacing, and outputs a custom CSS layout based on user-defined parameters such as image size, link distance, and font size.

## Features

- Calculates the positions of links around a circular image.
- Ensures a minimum distance between the circle and the surrounding links.
- Generates a CSS file with all necessary styling and positioning.
- Fully customizable parameters for image size, font size, padding, and margin.

## Installation

To use this tool:

1. Clone the repository

2. Ensure you have Python 3.x installed on your machine.

## Usage

1. Open the `script.py` file in any text editor and adjust the following parameters if needed:

   - **image_size**: The size of the central image (width and height in pixels).
   - **link_distance**: The minimum desired distance between the circle and the links (in pixels).
   - **font_size**: The size of the font for the link labels (in pixels).
   - **horizontal_padding**: Padding around the link text (horizontally, in pixels).
   - **vertical_padding**: Padding around the link text (vertically, in pixels).
   - **margin**: The margin around the entire content (in pixels).
   - **css_file_path**: The CSS file final path.
   
2. After setting the parameters, run the script:

   ```bash
   python script.py
   ```

3. The script will generate a CSS file. This file contains all the CSS rules for positioning the links around the circle.

4. Add the generated CSS file to your web project by linking it in your HTML file.

## Example

The script comes with an example configuration for six links:

```python
links = [
    {"titre": "Moi-même", "url": "moi.html"},
    {"titre": "Curriculum Vitae", "url": "cv.html"},
    {"titre": "Projets divers", "url": "projets.html"},
    {"titre": "Me contacter", "url": "contact.html"},
    {"titre": "Livre d'or", "url": "livre-d-or.html"},
    {"titre": "Implant", "url": "FLEXNT.html"}
]
```

These links will be positioned around a central circular image and styled according to the CSS generated by the script.

## Output

- The output of the script is a CSS file, which contains all the necessary styling and positioning rules for a circular link menu.
- In addition, the script prints the minimum distances between the circle and each link to the console.

## Example of generated nav
I added my own css on top of it. (Not finished)
![2024-10-13 09 15 03](https://github.com/user-attachments/assets/e14d2ed6-e40c-4ee1-942f-c4565b75b2cf)

## License

This project is licensed under no license whatsoever, do what you want I don't care. Thx
