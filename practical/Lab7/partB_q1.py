from PIL import Image
import pytesseract

# Path to tesseract executable (set this path if necessary)
# Example for Windows:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image
image_path = 'download.jpeg'
image = Image.open(image_path)

# Use pytesseract to extract text
extracted_text = pytesseract.image_to_string(image)

# Print extracted text
print("Extracted Text:")
print(extracted_text)
