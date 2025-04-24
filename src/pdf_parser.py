import pytesseract
from pdf2image import convert_from_path
import json

# Convert PDF pages to images
pages = convert_from_path('invoice_recHWC7qGba0eRogA.pdf')

data = []
for page in pages:
    text = pytesseract.image_to_string(page)
    data.append({'page_text': text})

# Save as JSON
with open('tesseract-output.json', 'w') as f:
    json.dump(data, f, indent=2)
