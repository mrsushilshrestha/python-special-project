import qrcode
import cv2
from pyzbar.pyzbar import decode
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Function to generate QR code
def generate_qr():
    data = entry.get()
    if not data:
        messagebox.showerror("Error", "Please enter data to generate QR code")
        return
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save("generated_qr.png")

    # Display the generated QR code
    img = Image.open("generated_qr.png")
    img = img.resize((200, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    qr_label.config(image=img)
    qr_label.image = img
    messagebox.showinfo("Success", "QR Code Generated and saved as 'generated_qr.png'")

# Function to scan QR code from an image
def scan_qr_from_image():
    file_path = filedialog.askopenfilename(title="Select a QR Code Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")])
    if file_path:
        img = cv2.imread(file_path)
        decoded_objects = decode(img)
        for obj in decoded_objects:
            qr_data = obj.data.decode("utf-8")
            messagebox.showinfo("QR Code Scanned", f"Scanned Data: {qr_data}")
            return
        messagebox.showerror("Error", "No QR code found in the image")

# Function to scan QR code using webcam
def scan_qr_using_camera():
    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        decoded_objects = decode(frame)
        for obj in decoded_objects:
            qr_data = obj.data.decode("utf-8")
            messagebox.showinfo("QR Code Scanned", f"Scanned Data: {qr_data}")
            cap.release()
            cv2.destroyAllWindows()
            return
        cv2.imshow("QR Code Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()

# GUI Setup
root = tk.Tk()
root.title("QR Code Generator & Scanner")
root.geometry("400x500")

tk.Label(root, text="Enter text or URL:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=5)

tk.Button(root, text="Generate QR", command=generate_qr, font=("Arial", 12), bg="green", fg="white").pack(pady=10)

qr_label = tk.Label(root)
qr_label.pack()

tk.Button(root, text="Scan QR from Image", command=scan_qr_from_image, font=("Arial", 12), bg="blue", fg="white").pack(pady=10)
tk.Button(root, text="Scan QR Using Camera", command=scan_qr_using_camera, font=("Arial", 12), bg="blue", fg="white").pack(pady=10)

root.mainloop()
