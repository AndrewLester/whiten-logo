from PIL import Image
import argparse

parser = argparse.ArgumentParser(prog="whiten-logo",
                                 description="Whiten a logo",
                                 epilog="Successfully whitened",
                                 argument_default=None,
                                 add_help=True)

parser.add_argument('input')
parser.add_argument('--output', default='whitened.png')

args = parser.parse_args()

image = Image.open(args.input)

image = image.copy()

WHITE = (255, 255, 255, 255)
for x in range(image.width):
    for y in range(image.height):
        pixel = image.getpixel((x, y))
        # If white, make transparent
        if pixel == WHITE:
            image.putpixel((x, y), (255, 255, 255, 0))
        # If colorful, make white
        elif pixel[3] != 0:
            # You may wish to change this line to make colorful pixels 100% white by replacing pixel[3] with 255
            # This will mess up antialiasing on edges of shapes, so uncomment the lines on 32-35 to correct
            image.putpixel((x, y), (255, 255, 255, pixel[3]))

# Image must be downsized to anti-alias the now jagged edges
# scale = 7 / 8
# image = image.resize((int(image.width * scale), int(image.height * scale)),
#                      resample=Image.ANTIALIAS)
image.save(args.output)
