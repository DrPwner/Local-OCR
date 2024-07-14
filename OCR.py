import time
import os
import pyautogui
import pytesseract
from PIL import Image
import pyperclip
from datetime import datetime

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Set the paths for screenshots and output
screenshots_folder = os.path.expanduser('~\\Pictures\\Screenshots')
output_folder = os.path.join(os.path.expanduser('~'), 'Documents', 'OCRTextExtract')

def get_latest_screenshot():
    try:
        files = [os.path.join(screenshots_folder, f) for f in os.listdir(screenshots_folder) if f.endswith('.png')]
        if not files:
            print("No screenshots found in the specified folder.")
            return None
        return max(files, key=os.path.getctime)
    except Exception as e:
        print(f"Error getting latest screenshot: {str(e)}")
        return None

def extract_text_from_image(image_path):
    try:
        with Image.open(image_path) as image:
            text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        print(f"Error extracting text from image: {str(e)}")
        return ""

def copy_to_clipboard(text):
    try:
        pyperclip.copy(text)
    except Exception as e:
        print(f"Error copying to clipboard: {str(e)}")

def save_text_to_file(text, screenshot_name):
    try:
        now = datetime.now()
        date_time = now.strftime("%Y%m%d_%H%M%S")
        file_name = f"{os.path.splitext(os.path.basename(screenshot_name))[0]}_{date_time}.txt"
        
        os.makedirs(output_folder, exist_ok=True)
        
        file_path = os.path.join(output_folder, file_name)
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)
        
        print(f"Text saved to: {file_path}")
    except Exception as e:
        print(f"Error saving text to file: {str(e)}")

def main():
    try:
        # Simulate Windows + Shift + S to open Snipping Tool
        pyautogui.hotkey('winleft', 'shift', 's')
        
        # Wait for the user to make a selection and for the screenshot to be saved
        time.sleep(4)
        
        # Get the latest screenshot
        latest_screenshot = get_latest_screenshot()
        if latest_screenshot is None:
            print("No screenshot found. Please try again.")
            return
        
        # Extract text from the screenshot
        extracted_text = extract_text_from_image(latest_screenshot)
        
        if not extracted_text:
            print("No text could be extracted from the image. Please try again.")
            return
        
        # Copy text to clipboard
        copy_to_clipboard(extracted_text)
        
        # Save text to file
        save_text_to_file(extracted_text, latest_screenshot)
        
        print("Text extracted, copied to clipboard, and saved to file.")
    except Exception as e:
        print(f"Error in main function: {str(e)}")
        print("An error occurred. Please try again.")

if __name__ == "__main__":
    main()
