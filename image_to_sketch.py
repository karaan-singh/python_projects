import tkinter as tk
from tkinter import filedialog, Text, Scrollbar, messagebox
from PIL import Image, ImageTk
import pytesseract
import cv2

# Path to tesseract executable (Change this for Windows users)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# --- Function to upload image ---
def upload_image():
    global img_path, img_display
    img_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.tiff")]
    )
    if img_path:
        # Open and display the image
        img = Image.open(img_path)
        img = img.resize((300, 250))  # Resize for preview
        img_display = ImageTk.PhotoImage(img)
        panel.config(image=img_display)
        panel.image = img_display

# --- Function to extract text ---
def extract_text():
    if not img_path:
        messagebox.showwarning("Warning", "Please upload an image first.")
        return
    
    # Load image with OpenCV
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # OCR extraction
    text = pytesseract.image_to_string(gray)

    # Show result in text box
    text_box.delete(1.0, tk.END)  # Clear previous text
    text_box.insert(tk.END, text)

# --- Tkinter GUI setup ---
root = tk.Tk()
root.title("Image to Text Converter")
root.geometry("600x500")
root.config(bg="#2c2c2c")

# Upload button
upload_btn = tk.Button(root, text="Upload Image", command=upload_image, bg="#4CAF50", fg="white", font=("Arial", 12))
upload_btn.pack(pady=10)

# Image preview panel
panel = tk.Label(root, bg="#2c2c2c")
panel.pack()

# Extract button
extract_btn = tk.Button(root, text="Extract Text", command=extract_text, bg="#2196F3", fg="white", font=("Arial", 12))
extract_btn.pack(pady=10)

# Text box with scrollbar
frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_box = Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set, width=70, height=10, font=("Arial", 10))
text_box.pack()

scrollbar.config(command=text_box.yview)

# Run Tkinter loop
img_path = ""  # Global variable to store image path
root.mainloop()