import PIL
from PIL import Image, ImageEnhance
import numpy

picture = PIL.Image.open('saturn.jpeg')
enhancer = ImageEnhance.Contrast(picture)
picture = enhancer.enhance(8)

ascii_brightness = {
    0: '@', 10: '#', 20: '8', 30: '&', 40: '%', 50: 'B', 60: 'W', 70: 'M',
    80: 'X', 90: 'Q', 100: 'O', 110: 'Z', 120: '0', 130: 'U', 140: 'J',
    150: 'L', 160: 'C', 170: 'Y', 180: 'u', 190: 'n', 200: 'x', 210: 'r',
    220: 'j', 230: 'f', 240: 't', 250: '-', 255: ' '
}

chars = numpy.array(list(ascii_brightness.values()))
new_width = 1100
width, height = picture.size
new_height = max(1, int(height / width * new_width * 0.3))

new_picture = picture.resize((new_width, new_height)).convert('L')
pixel_matrix = numpy.array(new_picture)
index_matrix = (pixel_matrix / 256 * len(chars)).astype(int)

ascii_matrix = chars[index_matrix]
final_string = ''
for row in ascii_matrix:
    line = "".join(row)
    final_string += line + "\n"

with open("test.txt", "w", encoding="utf-8") as f:
    f.write(final_string)