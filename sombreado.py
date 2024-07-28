import tkinter as tk
from tkinter import Canvas
from PIL import ImageGrab
from TraductorImagenes import TraductorImagenes

class ScreenSelector:
    def __init__(self, root, rootTranslated):
        self.root = root
        self.root.attributes('-fullscreen', True)
        self.root.bind("<ButtonPress-1>", self.on_button_press)
        self.root.bind("<B1-Motion>", self.on_mouse_drag)
        self.root.bind("<ButtonRelease-1>", self.on_button_release)
        #self.root.attributes('-transparentcolor', 'white')  # Transparente para el color blanco
        self.root.attributes('-alpha', 0.1)
        
        self.canvas = Canvas(root, bg="white", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.start_x = None
        self.start_y = None
        self.rect_id = None
        self.selection = None

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        if self.rect_id:
            self.canvas.delete(self.rect_id)
        self.rect_id = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline="gray", fill="gray", stipple="gray50")

    def on_mouse_drag(self, event):
        cur_x, cur_y = event.x, event.y
        self.canvas.coords(self.rect_id, self.start_x, self.start_y, cur_x, cur_y)

    def on_button_release(self, event):
        end_x, end_y = event.x, event.y
        self.canvas.delete(self.rect_id)
        self.rect_id = None

        # Save the selected area
        x1, y1 = min(self.start_x, end_x), min(self.start_y, end_y)
        x2, y2 = max(self.start_x, end_x), max(self.start_y, end_y)
        self.save_screenshot(x1, y1, x2, y2)

    def save_screenshot(self, x1, y1, x2, y2):
        # Take a screenshot of the entire screen
        bbox = (x1, y1, x2, y2)
        screenshot = ImageGrab.grab(bbox)
        translator = TraductorImagenes(screenshot)
        
        text = translator.translate()
        label = tk.Label(rootTranslated,text=text)
        label.pack(pady=20)
        screenshot.save("test.png")
        # print("La región seleccionada se ha guardado como 'test.png'.")

if __name__ == "__main__":
    root = tk.Tk()
    rootTranslated = tk.Tk()
    app = ScreenSelector(root,rootTranslated)
    rootTranslated.mainloop()
    root.mainloop()
