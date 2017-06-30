from PIL import Image

# RGB values for recoloring.
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

recolor = []
# Import image.
my_image = Image.open("flower.jpg") #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

for pixel in image_list:
    pixel_intensity = pixel[0] + pixel[1] + pixel[2]
    if pixel_intensity < 182:
        pixel = darkBlue
        recolor.append(pixel)
    elif pixel_intensity >= 182 and pixel_intensity <= 364:
        pixel = red
        recolor.append(pixel)
    elif pixel_intensity >= 364 and pixel_intensity <= 546:
        pixel = lightBlue
        recolor.append(pixel)
    elif pixel_intensity >546:
        pixel = yellow
        recolor.append(pixel)
 #list that will hold the pixel data for the new image.

#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.



# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolor) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"
