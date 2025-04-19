
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from rembg import remove
from io import BytesIO

class ImageConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("JPG to Transparent PNG Converter")

        self.input_img_label = tk.Label(root, text="Original Image")
        self.input_img_label.pack()
        self.input_img_canvas = tk.Label(root)
        self.input_img_canvas.pack()

        self.output_img_label = tk.Label(root, text="Converted PNG")
        self.output_img_label.pack()
        self.output_img_canvas = tk.Label(root)
        self.output_img_canvas.pack()

        self.select_btn = tk.Button(root, text="Select JPG Image", command=self.select_image)
        self.select_btn.pack(pady=10)

        self.save_btn = tk.Button(root, text="Save PNG", command=self.save_image, state=tk.DISABLED)
        self.save_btn.pack(pady=10)

        self.input_image_data = None
        self.output_image_data = None

    def select_image(self):
        filepath = filedialog.askopenfilename(filetypes=[("JPG files", "*.jpg;*.jpeg")])
        if not filepath:
            return

        try:
            # Load input image
            with open(filepath, "rb") as f:
                self.input_image_data = f.read()

            # Remove background
            self.output_image_data = remove(self.input_image_data)

            # Show images
            self.display_image(self.input_image_data, self.input_img_canvas)
            self.display_image(self.output_image_data, self.output_img_canvas)

            self.save_btn.config(state=tk.NORMAL)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_image(self, img_data, canvas_label):
        img = Image.open(BytesIO(img_data)).convert("RGBA")
        img.thumbnail((300, 300))
        img_tk = ImageTk.PhotoImage(img)
        canvas_label.config(image=img_tk)
        canvas_label.image = img_tk

    def save_image(self):
        if not self.output_image_data:
            return
        filepath = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png")])
        if filepath:
            with open(filepath, "wb") as f:
                f.write(self.output_image_data)
            messagebox.showinfo("Saved", f"Image saved to: {filepath}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageConverterApp(root)
    root.mainloop()
