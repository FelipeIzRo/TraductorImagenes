import tkinter as tk
from tkinter import Canvas
from PIL import ImageGrab
from TraductorImagenes import TraductorImagenes
import time
# from VentanaPrincipal import VentanaPrincipal

import pytesseract
from googletrans import Translator

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class ScreenSelector:

    def __init__(self, main_window):
        self.root=tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.bind("<ButtonPress-1>", self.on_button_press)
        self.root.bind("<B1-Motion>", self.on_mouse_drag)
        self.root.bind("<ButtonRelease-1>", self.on_button_release)
        #self.root.attributes('-transparentcolor', 'white')  # Transparente para el color blanco
        self.root.attributes('-alpha', 0.1)
        
        self.canvas = Canvas(self.root, bg="white", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.start_x = None
        self.start_y = None
        self.rect_id = None
        self.selection = None

        self.x1= None
        self.x2= None
        self.y1= None
        self.x2= None

        self.main_window = main_window

        self.bbox = None


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
        self.x1, self.y1 = min(self.start_x, end_x), min(self.start_y, end_y)
        self.x2, self.y2 = max(self.start_x, end_x), max(self.start_y, end_y)
        self.bbox = (self.x1, self.y1, self.x2, self.y2)
        self.save_screenshot()

    def save_screenshot(self):
        # Take a screenshot of the entire screen
        try:
            screenshot = ImageGrab.grab(self.bbox)
        
            translator = TraductorImagenes(screenshot)
            text = translator.translate()
            self.main_window.LabelTranslated(text)
        except:
            print('Error capturar imagen')
        finally:
            self.root.after(1000, self.save_screenshot)
        
        # screenshot.save("test.png")
        # print("La región seleccionada se ha guardado como 'test.png'.")
        # self.root.destroy() 

        