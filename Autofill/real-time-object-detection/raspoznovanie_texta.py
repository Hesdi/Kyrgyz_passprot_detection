import cv2
import easyocr

# Read the image
image_path = 'C:/Users/abdul/Documents/.Prog/Course2/Autofill/images/1658119050410.jpg'
img = cv2.imread(image_path)

# Resize the image to a specific height (e.g., 800 pixels)
desired_height = 800
aspect_ratio = img.shape[1] / img.shape[0]
desired_width = int(desired_height * aspect_ratio)
resized_img = cv2.resize(img, (desired_width, desired_height))

# Proceed with EasyOCR on the resized image
reader = easyocr.Reader(['en', 'ru'])
results = reader.readtext(resized_img)
print(results)
