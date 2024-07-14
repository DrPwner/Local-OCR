# Local OCR Text Extractor

## Purpose

This project provides a local Optical Character Recognition (OCR) solution for extracting text from confidential images. It's designed for situations where you need to select and copy text from sensitive images without uploading them to external services, ensuring data privacy and confidentiality.

## Features

- Uses Windows Snipping Tool for screenshot capture
- Performs OCR on the captured screenshot
- Copies extracted text to clipboard
- Saves extracted text to a file for backup and longer text storage

## How It Works

1. The script simulates the Windows + Shift + S keyboard shortcut to open the Snipping Tool.
2. After the user selects an area and captures the screenshot, the script waits for a few seconds.
3. It then locates the most recent screenshot in the user's Pictures/Screenshots folder.
4. The script performs OCR on this screenshot using Tesseract OCR.
5. The extracted text is copied to the clipboard for immediate use.
6. The text is also saved to a file in case it's too long for the clipboard or for future reference.

## Text Storage

- Clipboard: The extracted text is immediately copied to the clipboard for quick access.
- Text File: A text file is created in the user's Documents/OCRTextExtract folder.
  - File Naming Convention: `[OriginalScreenshotName]_[YYYYMMDD_HHMMSS].txt`
  - This ensures that each extraction creates a unique file, even if multiple extractions are performed on the same screenshot.

## Requirements

- Python 3.x
- Tesseract OCR installed on the system
- Python libraries: pyautogui, pytesseract, Pillow, pyperclip

## Setup

1. Install Tesseract OCR:
   - Download the Tesseract executable from [UB-Mannheim's GitHub repository](https://github.com/UB-Mannheim/tesseract/wiki)
   - Install Tesseract and note down the installation path
2. Install required Python libraries:
   - pip install pyautogui pytesseract Pillow pyperclip pyinstaller

3. Update the `pytesseract.pytesseract.tesseract_cmd` path in the script. For example:

  ``` pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" ```

## Usage

### Method 1: Running the Python Script

Run the script:
``` python ocr_text_extractor.py ```

### Method 2: Compiled Executable with Keyboard Shortcut (Recommended)

1. Compile the script into an executable:
``` pyinstaller --onefile --noconsole OCR.py ```
2. Create a shortcut to the generated "OCR.exe" file.
3. Right-click on the shortcut, select Properties, and set a keyboard shortcut (e.g., Ctrl + Alt + E) in the "Shortcut key" field.
4. Place the shortcut in a convenient location (e.g., Desktop or Startup folder for automatic startup).

Now you can use the keyboard shortcut (Ctrl + Alt + E) to execute the OCR tool whenever needed.

After activation, use the Snipping Tool to select the area containing the text you want to extract. The script will automatically process the screenshot and extract the text.

## Note

This tool is designed for local use to maintain confidentiality. Ensure you have the necessary permissions to capture and process the images you're working with.


