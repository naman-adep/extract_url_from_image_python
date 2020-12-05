# Importing packages
from PIL import Image 
import pytesseract
import cv2
import re
import os 
import webbrowser

# Reading the image using cv2
img = cv2.imread("url.png") 

# Converting the image to grayscale 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Creating a temporary file to store the grayscale image using os
file = "{}.png".format(os.getpid())
cv2.imwrite(file, gray)

# Extracting thr string from the image using pytesseract
text = pytesseract.image_to_string(Image.open(file))
# Removing the temporary file we created  
os.remove(file)

# Extracting the url from the string ex
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[.]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)

print(urls[0])

webbrowser.open(urls[0])