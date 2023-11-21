from PIL import Image

image = Image.open("grayscaleImage.png")

width, height = image.size

new_image = Image.new('L', (width, height))

pixels = new_image.load()

def greyscaleToBinary(image):

    max_pixel = 0
    min_pixel = 256

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))

            if pixel > max_pixel:
                max_pixel = pixel
            if pixel < min_pixel:
                min_pixel = pixel

    threshold = (max_pixel-min_pixel)/2
    print("Highest pixel:", max_pixel, "Lowest pixel:", min_pixel, "Threshold:", threshold)

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))

            if pixel >= threshold:
                new_pixel = 255
            else:
                new_pixel = 0

            pixels[x, y] = new_pixel

    new_image.save('binaryscaleImage.png')

    new_image.show()

greyscaleToBinary(image)