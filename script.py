import math
import os

# Parameters
image_size = 250  # Size of the image (width and height in pixels)
link_distance = 20  # Minimum desired distance between the circle and the links (in pixels)
font_size = 22  # Font size in pixels
horizontal_padding = 10  # Horizontal padding on each side (in pixels)
vertical_padding = 5  # Vertical padding on top and bottom (in pixels)
margin = 20  # Margin around the content (in pixels)
css_file_path = 'PATH/TO/THE/FINAL.css' # Save the CSS file in the specified directory

# List of links with their titles and URLs
links = [
    {"title": "Myself", "url": "myself.html"},
    {"title": "Curriculum Vitae", "url": "cv.html"},
    {"title": "Projects", "url": "projets.html"},
    {"title": "Contact Me", "url": "contact.html"},
]

# Function to estimate text width based on font size
def estimate_text_width(text, font_size):
    # Assuming an average character width of about 0.6 times the font size
    return len(text) * font_size * 0.6

# Initial calculations
number_of_links = len(links)
radius_image = image_size / 2

# Store link positions and minimum distances
link_positions = []
minimum_distances = []

# Calculate positions and distances for each link
for i, link in enumerate(links):
    # Adjust angle to start at 180 degrees and distribute in a clockwise direction
    angle_deg = 180 - i * (360 / number_of_links)
    angle_rad = math.radians(angle_deg)
    
    # Estimate link dimensions
    text_width = estimate_text_width(link['title'], font_size)
    link_width = text_width + horizontal_padding * 2
    link_height = font_size + vertical_padding * 2

    # Half dimensions
    L = link_width / 2
    H = link_height / 2

    # Directional components
    a = abs(math.cos(angle_rad))
    b = abs(math.sin(angle_rad))

    # Total desired distance
    D = radius_image + link_distance

    # Calculate effective radius for positioning the link
    effective_radius = D + L * a + H * b

    # Position the link based on the calculated angle and effective radius
    x_pos = effective_radius * math.cos(angle_rad)
    y_pos = -effective_radius * math.sin(angle_rad)

    # Store the position
    link_positions.append({"x": x_pos, "y": y_pos, "width": link_width, "height": link_height, "index": i})

    # Calculate the minimum distance between the circle and the nearest point of the link
    distance_to_circle = effective_radius - (L * a + H * b)
    minimum_distances.append(distance_to_circle)

# Calculate the maximum dimensions for the container
max_L = max([pos['width']/2 for pos in link_positions]) if link_positions else 0
max_H = max([pos['height']/2 for pos in link_positions]) if link_positions else 0
max_distance = radius_image + link_distance + max_L + max_H

container_width = 2 * max_distance + margin * 2
container_height = 2 * max_distance + margin * 2

# Center of the container
center_x = container_width / 2
center_y = container_height / 2

# Generate the CSS content
css_content = f"""#menu-container {{
    position: relative;
    width: {container_width:.2f}px;
    height: {container_height:.2f}px;
    margin: 0 auto;
}}

#center-image {{
    position: absolute;
    top: 50%;
    left: 50%;
    width: {image_size}px;
    height: {image_size}px;
    transform: translate(-50%, -50%);
}}

#menu {{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
    list-style: none;
}}

.menu-item {{
    position: absolute;
    transform: translate(-50%, -50%);
    white-space: nowrap;
}}

.menu-item a {{
    font-size: {font_size}px;
    padding: {vertical_padding}px {horizontal_padding}px;
}}

"""

# Add link positions to the CSS
for pos in link_positions:
    x_css = center_x + pos['x']
    y_css = center_y + pos['y']
    css_content += f""".menu-item.item{pos['index']} {{
    left: {x_css:.2f}px;
    top: {y_css:.2f}px;
}}\n"""

# Save the CSS file in the specified directory
os.makedirs(os.path.dirname(css_file_path), exist_ok=True)
with open(css_file_path, 'w') as css_file:
    css_file.write(css_content)

# Output minimum distances to the console
print("\nMinimum distances between the circle and the nearest point of each link:")
for i, distance in enumerate(minimum_distances):
    print(f"Link {i+1} ({links[i]['title']}): {distance:.2f}px")

print(f"\nThe CSS file has been generated and saved at '{css_file_path}'.")
