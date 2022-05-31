# font-project
 
Small test project to have fun with Python Imaging Library. The goal was to create an image off of a message "Cramik" and a collection of TrueType and OpenType font files (116k or so). output1.png was generated with font size 11 and output2.png with size 33 (multiplied all the constants by 3 [other than the division by two for xText])

Things I learned:
- JPEG and WEBP both have really constricting image dimension limits compared to PNG
- Drawing images with python is pretty easy
- Github has a 50mb free file limit, but also has Git Large File Storage which increases that limit to 2GB
- Font size standardization remains largely unfollowed

Things I didn't learn:
- Why "from PIL import *" didnt work. If you know why, please let me know


EDIT:
I just realized, I could probably get it within the size constraints of JPEG if I chose to make it a square, instead of a very long image. I don't know if I care enough to try doing that
