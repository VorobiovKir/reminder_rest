from PIL import Image

img = Image.open('media/origin/Metallica-logo.jpg')
print img.size
print 'hello'
size = (35, 35)
img.thumbnail(size)
img.save('media/thumbnail/metallica-logo.jpg', 'JPEG')
