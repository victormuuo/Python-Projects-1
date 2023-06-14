#install pillow
#import pillow
#open the image you want to resize with python
#print the current size of that image
#specify the size you want to change it to
#save the new resized image

from PIL import Image

def resize_image(size1,size2):
    image=Image.open('kanyeee.jpg')

    print(f"Current size: {image.size}")

    resized_image=image.resize((size1,size2))
    resized_image.save('victor-praise-the-lord'+ str(size1) + '.jpeg')

size1=int(input("Enter Width: "))
size2=int(input("Enter Length: "))
resize_image(size1,size2)

