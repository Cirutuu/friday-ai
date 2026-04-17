import tkinter as tk
import math
import time

def show_glow():
    root = tk.Tk()
    root.title("Friday")
    root.attributes("-topmost", True)
    root.overrideredirect(True)
    root.config(bg="black")

    width, height = 400, 400
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

    canvas = tk.Canvas(root, width=width, height=height, bg="black", highlightthickness=0)
    canvas.pack()

    cx, cy = width // 2, height // 2

    core = canvas.create_oval(cx-40, cy-40, cx+40, cy+40, outline="cyan", width=3)
    ring = canvas.create_oval(cx-120, cy-120, cx+120, cy+120, outline="cyan", width=2)

    start_time = time.time()
    angle = 0

    def animate():
        nonlocal angle

        t = time.time() - start_time

        # 🔵 breathing pulse
        pulse = 40 + 10 * math.sin(t * 3)
        canvas.coords(core, cx-pulse, cy-pulse, cx+pulse, cy+pulse)

        # 🌀 rotating dash illusion
        canvas.itemconfig(ring, dash=(5, 2), dashoffset=angle)
        angle += 2

        # loop animation
        root.after(20, animate)

    animate()

    # auto close after 3 sec
    root.after(3000, root.destroy)

    root.mainloop()
