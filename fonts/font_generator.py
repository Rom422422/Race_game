"""
Code from Maxime BARTHOMEUF
"""

from PIL import Image, ImageDraw, ImageFont

# Use Exemple
offset_x = 0
offset_y = 50
ascii_offset = 32  # We want to starts with the "!"
end_ascii = 126
background_color = (0, 0, 0, 0)  # Transparent
font_color = (255, 255, 255)  # White
font_color = (35, 30, 139) # Blue
font_color= (186 ,17 ,203 ) # Purple
font_color = (17,14,71) # Dark Blue
font_color = (178,175,250) # Light Blue
font_color = (241,49,71) # Red
font_size = 200
image_path = "fontCB_Red.png"


# Image configuration
num_lines = 5
num_chars_per_line = 30

# Image creation
img = Image.new('RGBA', (num_chars_per_line * font_size, num_lines * font_size), color=background_color)
d = ImageDraw.Draw(img)

# Creation of the font with the specified size and a font by default
font = ImageFont.truetype("Cross Boxed.ttf", font_size)

# Characters display
for i in range(num_lines):
    for j in range(num_chars_per_line):
        if ascii_offset + i * num_chars_per_line + j >= end_ascii:
            break
        char = chr(ascii_offset + i * num_chars_per_line + j)
        d.text((j * font_size + offset_x, i * (font_size + 2)+ offset_y), char, fill=font_color, font=font)

# Revert the image to have a vertical flip
img = img.transpose(Image.FLIP_TOP_BOTTOM)

# Save of the image
img.save(image_path)