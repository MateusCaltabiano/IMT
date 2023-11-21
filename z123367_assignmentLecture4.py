from PIL import Image

image = Image.open("grayscaleImage.png").convert("L")

width, height = image.size

new_image = Image.new("L", (width, height))

pixels = new_image.load()

def gaussianFilter(image, pixelPositionX, pixelPositionY):
    pixelNeighbors = [[0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0]]
    i = 0
    j = 0
    sum = 0
    gFilter = [[1, 1, 2, 1, 1],
               [1, 2, 4, 2, 1],
               [2, 4, 8, 4, 2],
               [1, 2, 4, 2, 1],
               [1, 1, 2, 1, 1]]
    for x in range(pixelPositionX - 2, pixelPositionX + 3):
        for y in range(pixelPositionY - 2, pixelPositionY + 3):
            pixelNeighbors[i][j] = image.getpixel((x, y))
            j = j+1
        j = 0
        i = i+1


    for x in range(5):
        for y in range(5):
            sum += pixelNeighbors[x][y]*gFilter[x][y]
    return int(sum/48)

def applyGaussianFilter(image):
    for x in range(2, width-2):
        for y in range(2, height-2):
            pixels[x, y] = gaussianFilter(image, x, y)

applyGaussianFilter(image)

new_image.save("gaussianFilterImage.png")
image.show()
new_image.show()