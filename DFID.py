import tkinter as tk
from tkinter import filedialog, scrolledtext
import threading
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Path to your Keras model
MODEL_PATH = r"C:\Users\Admin\Desktop\bestmodel\bestmodel.keras"

# Load the model globally when the app starts
model = load_model(MODEL_PATH)

# Preprocessing function for the image (adjust according to your model)
def detect_deepfake(image_path):
    try:
        # Load and preprocess the image
        img = image.load_img(image_path, target_size=(128, 128))  # Resize to model input size
        img_array = image.img_to_array(img)  # Convert to array
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        img_array = img_array / 255.0  # Normalize if the model was trained with normalization

        # Predict using the model
        prediction = model.predict(img_array)[0][0]

        # Interpret the result
        if prediction > 0.5:
            return "The image is Real."
        else:
            return "The image is Fake."
    except Exception as e:
        return f"Error during detection: {str(e)}"

class DeepFakeImageDetectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DeepFake Image Detector")
        self.root.configure(bg="#282a36")  # Dark background

        # Try to improve resolution scaling (works on some systems)
        self.root.tk.call('tk', 'scaling', 1.5)

        # Set window size to full screen, adjust with DPI
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        # Header label
        header_label = tk.Label(
            root,
            text="DeepFake Image Detector",
            font=("Arial", 32, "bold"),
            fg="white",
            bg="#282a36"
        )
        header_label.pack(pady=20)

        # Instruction label
        instruction_label = tk.Label(
            root,
            text="Upload an image for detection:",
            font=("Arial", 20),
            fg="light gray",
            bg="#282a36"
        )
        instruction_label.pack(pady=10)

        # Upload button
        self.upload_button = tk.Button(
            root,
            text="Choose File",
            font=("Arial", 18, "bold"),
            bg="#4682b4",
            fg="white",
            command=self.upload_file
        )
        self.upload_button.pack(pady=10)

        # Selected file label
        self.selected_file_label = tk.Label(
            root,
            text="No file selected",
            font=("Arial", 18, "italic"),
            fg="light gray",
            bg="#282a36"
        )
        self.selected_file_label.pack(pady=10)

        # Process button
        self.process_button = tk.Button(
            root,
            text="Detect DeepFake",
            font=("Arial", 18, "bold"),
            bg="#dc143c",
            fg="white",
            command=self.process_file
        )
        self.process_button.pack(pady=20)

        # Output area
        self.output_area = scrolledtext.ScrolledText(
            root,
            wrap=tk.WORD,
            font=("Courier New", 18),
            bg="#1e1e1e",
            fg="white",
            height=15,
            borderwidth=2,
            relief=tk.SOLID
        )
        self.output_area.insert(tk.END, "Output will appear here...")
        self.output_area.config(state=tk.DISABLED)
        self.output_area.pack(padx=50, pady=20, fill=tk.BOTH, expand=True)

        # Variable to store file path
        self.file_path = None

    def upload_file(self):
        self.file_path = filedialog.askopenfilename(
            title="Choose an Image File",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg"), ("All Files", "*.*")]
        )
        if self.file_path:
            self.selected_file_label.config(text=f"Selected: {self.file_path}")
            self.output_area.config(state=tk.NORMAL)
            self.output_area.delete(1.0, tk.END)
            self.output_area.insert(tk.END, f"File selected: {self.file_path}")
            self.output_area.config(state=tk.DISABLED)
        else:
            self.selected_file_label.config(text="No file selected")

    def process_file(self):
        if not self.file_path:
            self.output_area.config(state=tk.NORMAL)
            self.output_area.delete(1.0, tk.END)
            self.output_area.insert(tk.END, "Please select a file before processing.")
            self.output_area.config(state=tk.DISABLED)
        else:
            self.output_area.config(state=tk.NORMAL)
            self.output_area.delete(1.0, tk.END)
            self.output_area.insert(tk.END, "Processing the file...")
            self.output_area.config(state=tk.DISABLED)

            # Run the deepfake detection in a separate thread to prevent UI freezing
            threading.Thread(target=self.detect_and_update, args=(self.file_path,)).start()

    def detect_and_update(self, file_path):
        # Run the deepfake detection logic
        result = detect_deepfake(file_path)

        # Update the output area with the result
        self.output_area.config(state=tk.NORMAL)
        self.output_area.delete(1.0, tk.END)
        self.output_area.insert(tk.END, result)
        self.output_area.config(state=tk.DISABLED)

# Create the root window and run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = DeepFakeImageDetectorApp(root)
    root.mainloop()
