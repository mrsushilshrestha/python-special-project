import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import math
import random

# Create main window
root = tk.Tk()
root.title("Happy Valentine's Day ❤️")
root.geometry("500x600")
root.configure(bg="pink")

# Load Heart Image
heart_img = Image.open("image/heart.png")  # Ensure this image is available
heart_img = heart_img.resize((100, 100), Image.Resampling.LANCZOS)
heart_icon = ImageTk.PhotoImage(heart_img)

# Animated Heart
canvas = tk.Canvas(root, width=500, height=300, bg="pink", highlightthickness=0)
canvas.pack()
heart = canvas.create_image(250, 150, image=heart_icon)

# Heart Animation (beating effect)
def animate_heart():
    for i in range(30):
        scale_factor = 1 + 0.1 * math.sin(i / 5)  # Smooth scaling
        canvas.scale(heart, 250, 150, scale_factor, scale_factor)
        root.update()
        time.sleep(0.05)

# Floating Hearts Effect
floating_hearts = []
for _ in range(10):
    x = random.randint(50, 450)
    y = random.randint(200, 600)
    heart_floating = canvas.create_text(x, y, text="❤️", font=("Arial", 18))
    floating_hearts.append(heart_floating)

def float_hearts():
    while True:
        for heart in floating_hearts:
            canvas.move(heart, 0, -1)  # Move hearts upwards
            x, y = canvas.coords(heart)
            if y < 0:  # Reset position if it reaches top
                canvas.move(heart, 0, 600)
        root.update()
        time.sleep(0.05)

# Show Love Message
def show_love_message():
    messagebox.showinfo("💖 Happy Valentine's Day! 💖", 
                        "You are the love that makes my life beautiful.\n"
                        "Wishing you a day full of love and happiness! 💕")

# Stylish Button
btn = tk.Button(root, text="Click for a Surprise! 💘", font=("Arial", 14, "bold"),
                bg="#FF3B3F", fg="white", padx=10, pady=5, bd=3, relief="ridge",
                command=show_love_message)
btn.pack(pady=20)

# Run Animations
root.after(100, animate_heart)
root.after(100, float_hearts)

# Start Tkinter Loop
root.mainloop()
