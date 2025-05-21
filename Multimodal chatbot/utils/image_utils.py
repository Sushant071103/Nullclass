from PIL import Image
import google.generativeai as genai

# Already configured in config.py with API key
model = genai.GenerativeModel("gemini-1.5-pro")  # or "gemini-1.5-flash"

def analyze_image(image_file):
    image = Image.open(image_file)

    response = model.generate_content(
        [image, "Describe the image in detail."],
        stream=False
    )

    return response.text

