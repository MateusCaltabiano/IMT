from PIL import Image
import math

image = Image.open("grayscaleImage.png").convert("L")

width, height = image.size

new_image = Image.new("L", (width, height))

pixels = new_image.load()

kernelSize = int(input('please enter kernel size:\n'))

sigma = float(input("please enter sigma value:\n"))

def customizableGaussianFilter(image, pixelPositionX, pixelPositionY, kernelSize, sigma):
    weightedSum = 0
    gFilterSum = 0
    kernelCenter = (kernelSize-1)/2

    for x in range(pixelPositionX - int(kernelCenter), pixelPositionX + (int(kernelCenter) + 1)):
        for y in range(pixelPositionY - int(kernelCenter), pixelPositionY + (int(kernelCenter) + 1)):
            if x >= 0 and x < image.width and y >= 0 and y < image.height:
                pixel_value = image.getpixel((x, y))
                kernel_value = (1 / (2 * math.pi * sigma**2)) * math.exp(-((x - pixelPositionX)**2 + (y - pixelPositionY)**2) / (2 * sigma**2))
                gFilterSum += kernel_value
                weightedSum += pixel_value * kernel_value
            else:
                print(x, y, 'failed')
            
    return int(weightedSum/gFilterSum)

def applyGaussianFilter(image, kernelSize, sigma):
    for x in range(2, width-2):
        for y in range(2, height-2):
            pixels[x, y] = customizableGaussianFilter(image, x, y, kernelSize, sigma)

applyGaussianFilter(image, kernelSize, sigma)

new_image.save("gaussianFilterImageFinalTest.png")
image.show()
new_image.show()